from django.contrib import admin

from .models import Item


class ItemsAdmin(admin.ModelAdmin):
    """Создание представления модели в админ-панели"""
    list_display = ('pk', 'name', 'description', 'price', 'currency', )
    search_fields = ('name', )
    list_filter = ('name', 'price',)
    empty_value_display = '-empty-'


admin.site.register(Item, ItemsAdmin)
