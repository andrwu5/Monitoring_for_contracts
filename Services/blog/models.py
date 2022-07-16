from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver


class BlogPost(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    body = models.TextField(max_length=5000, null=False, blank=False, verbose_name="Сообщение")
    date_published = models.DateField(auto_now_add=True, verbose_name="Дата публикации")
    date_update = models.DateField(auto_now=True, verbose_name="Дата изменения")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")
    slug = models.SlugField(blank=True, unique=True, verbose_name="Краткий заголовок")

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блог"

    def _str_(self):
        return self.title

def pre_save_blog_post_receiever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + "-" + instance.title)
        
pre_save.connect(pre_save_blog_post_receiever, sender=BlogPost)

