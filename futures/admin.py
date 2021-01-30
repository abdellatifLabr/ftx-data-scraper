from django.contrib import admin

from .models import Future, Spread


@admin.register(Future)
class FutureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'updated_at')
    list_filter = ('name',)


@admin.register(Spread)
class SpreadAdmin(admin.ModelAdmin):
    list_display = ('pair_a', 'pair_b', 'buy_spread', 'sell_spread', 'created_at')
    list_filter = ('pair_a', 'pair_b')
