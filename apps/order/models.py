from django.db import models

from apps.catalog.models import Product
from apps.user.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Cart(models.Model):
    product = models.ForeignKey(to=Product, verbose_name='Продукт', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Кількість')
    user = models.ForeignKey(to=User, verbose_name='Покупець', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Кошик'
        verbose_name_plural = 'Кошики'


class Order(models.Model):
    user = models.ForeignKey(to=User, verbose_name='Покупець', on_delete=models.CASCADE)
    total = models.DecimalField(verbose_name='Всього', max_digits=12, decimal_places=2)
    first_name = models.CharField(verbose_name="Ім'я", max_length=255)
    last_name = models.CharField(verbose_name="Прізвище", max_length=255)
    email = models.EmailField(verbose_name='email')
    phone = PhoneNumberField(verbose_name='Телефон')
    address = models.TextField(verbose_name='Адрес')
    comment = models.TextField(verbose_name='Коментарій', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата редагування', auto_now=True)

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
