from django.db import models

from apps.catalog.models import Product
from apps.main.mixins import MetaTagMixin
from apps.user.models import User


class Cart(MetaTagMixin):
    product = models.ForeignKey(to=Product, verbose_name='Продукт', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Кількість')
    user = models.ForeignKey(to=User, verbose_name='Покупець', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Кошик'
        verbose_name_plural = 'Кошики'
