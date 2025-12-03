from django.urls import path
from .views import coin_ui, CoinListAPIView, health_check, api_home

urlpatterns = [
    path("", coin_ui, name="coin_ui"),
    path("home/", api_home),
    path("coins/", CoinListAPIView.as_view()),
    path("health/", health_check),
]
