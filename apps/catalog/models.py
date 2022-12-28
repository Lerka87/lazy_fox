from django.db import models
from django.utils.safestring import mark_safe
from imagekit.models import ProcessedImageField
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
from pilkit.processors import ResizeToFill

from config.settings import MEDIA_ROOT


class Category(MPTTModel):
    name = models.CharField(verbose_name='Назва', max_length=255)
    slug = models.SlugField(unique=True, verbose_name='Слаг (ЧПУ)')
    description = models.TextField(verbose_name='Опис', null=True, blank=True)
    image = ProcessedImageField(
        verbose_name='Картинка',
        upload_to='catalog/category/',
        processors=[ResizeToFill(600, 400)],
        null=True,
        blank=True
    )
    parent = TreeForeignKey(
        to='self',
        verbose_name='Родитель',
        related_name='child',
        on_delete=models.CASCADE,
        blank=True, null=True
    )

    def image_tag_thumbnail(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}' width='70'>")

    image_tag_thumbnail.short_description = 'Картинка'

    def image_tag(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}'>")

    image_tag.short_description = 'Наявна картинка'

    def __str__(self):
        full_path = [self.name]
        parent = self.parent
        while parent is not None:
            full_path.append(parent.name)
            parent = parent.parent
        return ' -> '.join(full_path[::-1])

    class Meta:
        verbose_name='Категорія',
        verbose_name_plural='Категорії'


class Product(models.Model):
    name = models.CharField(verbose_name='Назва', max_length=255)
    slug = models.SlugField(unique=True, verbose_name='Слаг (ЧПУ)', max_length=255)
    description = models.TextField(verbose_name='Опис', null=True, blank=True)
    quantity = models.IntegerField(verbose_name='кількість товару', null=True, blank=True)
    price = models.DecimalField(verbose_name='Ціна', max_digits=12, decimal_places=2, default=0)
    updated_at = models.DateTimeField(verbose_name='Дата зміни')
    created_at = models.DateTimeField(verbose_name='Дата створення')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Продукт'
        verbose_name_plural='Продукти'

