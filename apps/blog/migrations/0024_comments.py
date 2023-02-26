# Generated by Django 4.1.3 on 2023-02-26 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0023_rename_name_article_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('text', models.TextField(verbose_name='Текст')),
                ('publish_date', models.DateTimeField(verbose_name='Дата публікації')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Коментарій',
                'verbose_name_plural': 'Коментарії',
            },
        ),
    ]
