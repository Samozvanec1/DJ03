from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField('Название', max_length=128)
    short_desc = models.CharField('Краткое описание', max_length=256)
    content = models.TextField('Содержание', blank=True)
    user = models.CharField('Пользователь', blank=True, max_length=80)
    pub_date = models.DateTimeField('Дата публикации')
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
