# Generated by Django 4.1.3 on 2023-01-24 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0004_remove_cart_meta_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Всього')),
                ('first_name', models.CharField(max_length=255, verbose_name="Ім'я")),
                ('last_name', models.CharField(max_length=255, verbose_name='Прізвище')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Телефон')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Коментарій')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата редагування')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Покупець')),
            ],
            options={
                'verbose_name': 'Замовлення',
                'verbose_name_plural': 'Замовлення',
            },
        ),
    ]
