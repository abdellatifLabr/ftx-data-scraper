from django.contrib import admin

from .models import Future


@admin.register(Future)
class FutureAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'updated_at')
    list_filter = ('name',)
