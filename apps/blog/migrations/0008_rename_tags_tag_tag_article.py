# Generated by Django 4.1.3 on 2022-11-17 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_article_tags_tag_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='tags',
            new_name='tag_article',
        ),
    ]
