from django.db import models
from tinymce.models import HTMLField
from apps.main.mixins import MetaTagMixin


class Page(MetaTagMixin):
    name = models.CharField(verbose_name="Ім'я", max_length=255)
    slug = models.SlugField(unique=True)
    text = HTMLField(verbose_name='Вміст', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Інформаційна сторінка'
        verbose_name_plural = 'Інформаційні сторінки'
