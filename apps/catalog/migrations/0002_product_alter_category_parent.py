# Generated by Django 4.1.3 on 2022-12-28 09:24

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Слаг (ЧПУ)')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='кількість товару')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Ціна')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата зміни')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='catalog.category', verbose_name='Родитель'),
        ),
    ]
