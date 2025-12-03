# Create your models here.
from django.db import models

class Coin(models.Model):
    coin_id = models.CharField(max_length=100, unique=True)  # e.g. 'bitcoin'
    symbol = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    current_price = models.FloatField()
    formatted_price = models.CharField(max_length=50, default="0.00")
    market_cap = models.BigIntegerField(null=True, blank=True)
    last_updated = models.DateTimeField()

    def __str__(self):
        return f"{self.name} ({self.symbol})"
