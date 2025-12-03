from django.urls import path
from .views import health_check, CoinListAPIView, coin_ui
from . import views

urlpatterns = [
    path('health/', health_check),
    path('coins/', CoinListAPIView.as_view()),
    path('ui/', coin_ui),
    path('ui/', views.coin_ui, name='coins_dashboard'),
]
