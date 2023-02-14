from django.db import models


class Item(models.Model):
    """Модель товара"""
    currency_types = [
        ('usd', 'usd'),
        ('eur', 'eur')
    ]
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='name')
    description = models.TextField(max_length=250, blank=True, null=True, verbose_name='description')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='price')
    currency = models.CharField(max_length=3, choices=currency_types, verbose_name='currency', default='usd')

    def __str__(self):
        return self.name
