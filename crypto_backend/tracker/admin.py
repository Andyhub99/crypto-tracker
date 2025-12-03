from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Coin

@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ('name','symbol','current_price','market_cap','last_updated')
    search_fields = ('name','symbol','coin_id')
