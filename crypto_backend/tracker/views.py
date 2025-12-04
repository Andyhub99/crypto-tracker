from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils.timezone import now
from rest_framework import generics
from .models import Coin
from .serializers import CoinSerializer
import requests

# ------------------------------
# HEALTH CHECK
# ------------------------------
@api_view(['GET'])
def health_check(request):
    return Response({
        "health": "OK",
        "server_time": now(),
        "message": "Crypto Tracker backend running smoothly!"
    })

# ------------------------------
# COIN LIST API
# ------------------------------
class CoinListAPIView(generics.ListAPIView):
    queryset = Coin.objects.all().order_by('-market_cap')
    serializer_class = CoinSerializer

# ------------------------------
# COIN DASHBOARD UI
# ------------------------------
def coin_ui(request):
    return render(request, "coins.html")

# ------------------------------
# SPARKLINE / BAR CHART API
# ------------------------------
@api_view(['GET'])
def coin_sparkline(request, coin_id):
    """
    Returns recent price points (INR) for coin_id
    Query param: ?days=1
    """
    days = request.GET.get('days', '1')
    vs_currency = 'inr'
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": vs_currency, "days": days, "interval": "hourly"}

    try:
        r = requests.get(url, params=params, timeout=20)
        r.raise_for_status()
        data = r.json()
        prices = data.get("prices", [])
    except requests.RequestException as e:
        return Response({"error": "Failed to fetch from CoinGecko", "detail": str(e)}, status=502)

    return Response({"prices": prices})
