from django.contrib import admin
from apps.blog.models import BlogCategory, Article, Tag
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.utils.safestring import mark_safe


admin.site.register(Tag)


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image_tag_thumbnail', 'article_count']
    list_display_links = ['id', 'name', 'image_tag_thumbnail']
    fields = ['name', 'image_tag', 'image']
    readonly_fields = ['image_tag']

    def article_count(self, instance):
        articles = Article.objects.filter(category=instance).count()
        url = reverse('admin:blog_article_changelist') + '?' + urlencode({'category__id__exact': instance.id})
        return format_html(f'<a href="{url}">Статей: {articles}</a>')

    article_count.short_description = 'Кількість статей'


@admin.register(Article)
class ArticlaAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category_link', 'tag_list', 'created_at']
    list_display_links = ['id', 'title']
    list_filter = ['category', 'tag']

    def category_link(self, instance):
        url = reverse('admin:blog_blogcategory_change', args=[instance.category_id])
        return format_html(f"<a href='{url}'>{instance.category.name}</a>")

    category_link.short_description = 'Категорії'

    def tag_list(self, instance):
        tags = instance.tag.all()
        string_html = ''
        for i in range(len(tags)):
            string = str(tags[i])
            if i != 0:
                string_html += ', '
            string_html += f"<a href='{reverse('admin:blog_tag_change', args=[tags[i].id])}'>{string}</a>"
        if tags:
            return format_html(string_html)

    tag_list.short_description = 'Теги'

