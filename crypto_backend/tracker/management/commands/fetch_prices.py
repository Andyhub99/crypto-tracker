import requests
from django.core.management.base import BaseCommand
from tracker.models import Coin
from django.utils.dateparse import parse_datetime
from django.utils import timezone
from django.core.cache import cache

COINS = ["bitcoin", "ethereum", "dogecoin", "litecoin", "ripple"]

class Command(BaseCommand):
    help = "Fetch latest coin prices from CoinGecko and store/update in DB"

    def handle(self, *args, **options):
        vs_currency = "inr"  # Indian Rupees
        ids = ",".join(COINS)
        url = (
            f"https://api.coingecko.com/api/v3/coins/markets"
            f"?vs_currency={vs_currency}&ids={ids}&order=market_cap_desc&per_page=250&page=1&sparkline=false"
        )

        self.stdout.write(f"Requesting: {url}")
        try:
            r = requests.get(url, timeout=20)
            r.raise_for_status()
        except requests.RequestException as e:
            self.stderr.write(f"Request failed: {e}")
            return

        data = r.json()
        now_time = timezone.now()

        for item in data:
            coin_id = item.get('id')
            last_updated = parse_datetime(item.get('last_updated')) or now_time
            current_price = item.get('current_price') or 0.0

            # Format in Indian style with ₹ in front
            formatted_price = "₹{:,.2f}".format(current_price)  # ₹1,23,456.78

            obj, created = Coin.objects.update_or_create(
                coin_id=coin_id,
                defaults={
                    'symbol': item.get('symbol', '').upper(),
                    'name': item.get('name', ''),
                    'current_price': current_price,
                    'formatted_price': formatted_price,
                    'market_cap': item.get('market_cap') or 0,
                    'last_updated': last_updated,
                }
            )

            if created:
                self.stdout.write(f"Created {coin_id}: {formatted_price}")
            else:
                self.stdout.write(f"Updated {coin_id}: {formatted_price}")

        # Cache the last sync time (1 hour)
        cache.set("last_sync", now_time, 3600)
        self.stdout.write("Done.")
