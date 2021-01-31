from django.contrib import admin

from .models import Future, Spread, Pair


@admin.register(Future)
class FutureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'updated_at')
    list_filter = ('name',)


@admin.register(Pair)
class PairAdmin(admin.ModelAdmin):
    list_display = ('pair_a', 'pair_b')


@admin.register(Spread)
class SpreadAdmin(admin.ModelAdmin):
    list_display = ('pair', 'buy_spread', 'sell_spread', 'created_at')
    list_filter = ('pair',)
