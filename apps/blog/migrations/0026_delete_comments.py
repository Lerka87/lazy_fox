# Generated by Django 4.1.3 on 2023-02-26 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_comments_article'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comments',
        ),
    ]