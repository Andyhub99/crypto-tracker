from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils.timezone import now
from django.http import JsonResponse

# ------------------------------
# HOME API
# ------------------------------
@api_view(['GET'])
def api_home(request):
    return JsonResponse({
        "project": "Crypto Tracker API",
        "author": "Anuj (Andyhub99)",
        "signature": "Designed & Developed by Anuj Patil ✨",
        "status": "online",
        "timestamp": timezone.now().isoformat(),
        "endpoints": {
            "coins": "/api/coins/",
            "health": "/api/health/"
        }
    })


# ------------------------------
# HEALTH CHECK API
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
from rest_framework import generics
from .models import Coin
from .serializers import CoinSerializer

class CoinListAPIView(generics.ListAPIView):
    queryset = Coin.objects.all().order_by('-market_cap')
    serializer_class = CoinSerializer


# ------------------------------
# UI VIEW (HTML PAGE)
# ------------------------------
def coin_ui(request):
    return render(request, "coins.html")
