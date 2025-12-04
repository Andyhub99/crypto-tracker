from django.urls import path
from .views import health_check, CoinListAPIView, coin_ui, coin_sparkline

urlpatterns = [
    path('health/', health_check),
    path('coins/', CoinListAPIView.as_view()),
    path('ui/', coin_ui, name='coins_dashboard'),
    path('coins/<str:coin_id>/sparkline/', coin_sparkline),  # Sparkline API for bar charts
]
