# Generated by Django 4.1.3 on 2023-02-26 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_comments_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.AddField(
            model_name='comments',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="Ваше ім'я"),
        ),
    ]
