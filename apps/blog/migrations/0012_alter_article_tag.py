# Generated by Django 4.1.3 on 2022-11-19 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_article_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, to='blog.tag', verbose_name='Теги'),
        ),
    ]