from rest_framework import serializers
from .models import Coin

class CoinSerializer(serializers.ModelSerializer):
    price_category = serializers.SerializerMethodField()
    coin_id = serializers.CharField(source='id')
    formatted_price = serializers.SerializerMethodField()
    market_health = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Coin
        fields = [
            'id',
            'coin_id',
            'symbol',
            'name',
            'formatted_price',
            'market_cap',
            'last_updated',
            'price_category',
            'market_health',
            'rating'
        ]

    # ---------- PRICE IN INR ----------
    def get_formatted_price(self, obj):
        try:
            usd = obj.current_price
            inr = usd * 89.89  # Convert USD → INR (approx, stable)
            return f"₹{inr:,.2f}"
        except:
            return "N/A"

    # ---------- PRICE CATEGORY ----------
    def get_price_category(self, obj):
        if obj.market_cap > 200_000_000_000:
            return "🚀 High Market Cap"
        elif obj.market_cap > 50_000_000_000:
            return "📈 Mid Market Cap"
        return "🌱 Emerging Coin"

    # ---------- MARKET HEALTH ----------
    def get_market_health(self, obj):
        if obj.market_cap > 500_000_000_000:
            return "🔥 Strong Market Leader"
        elif obj.market_cap > 50_000_000_000:
            return "👍 Stable Performer"
        return "🟡 High Volatility Risk"

    # ---------- RATING ----------
    def get_rating(self, obj):
        if obj.market_cap > 200_000_000_000:
            return "A+"
        elif obj.market_cap > 100_000_000_000:
            return "A"
        elif obj.market_cap > 10_000_000_000:
            return "B"
        return "C"
