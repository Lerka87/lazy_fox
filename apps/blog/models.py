from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill


class BlogCategory(models.Model):
    name = models.CharField(verbose_name="Ім'я категорії", max_length=255)
    # image = models.ImageField(verbose_name='Картинка', upload_to='blog/categoty/', null=True)
    image = ProcessedImageField(
        verbose_name='Картинка',
        upload_to='blog/category/',
        processors=[ResizeToFill(600, 400)],
        null = True,
        blank=True
    )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія блога'
        verbose_name_plural = 'Категорії блога'



class Tag(models.Model):
    name = models.CharField(verbose_name="Напишіть сюди свій тег", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Article(models.Model):

    category = models.ForeignKey(to=BlogCategory, verbose_name='Категорія', on_delete=models.CASCADE)

    title = models.CharField(verbose_name='Заголовок', max_length=255)
    text_preview = models.TextField(verbose_name="Текст-прев'ю", null=True, blank=True)
    text = models.TextField(verbose_name='Текст')
    tag = models.ManyToManyField(to=Tag, verbose_name='Теги', blank=True)
    image = ProcessedImageField(
        verbose_name='Картинка',
        upload_to='blog/category/',
        null=True,
        blank=True
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 400)]
    )
    publish_date = models.DateTimeField(verbose_name='Дата публікації')
    updated_at = models.DateTimeField(verbose_name='Дата зміни', auto_now=True)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'