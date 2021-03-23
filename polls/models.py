from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField('分类', max_length=100)
    rank = models.IntegerField('级别', default=1)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField('标签', max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    intro = models.TextField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类', default='1')
    tags = models.ManyToManyField(Tags, blank=True)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    created_time = models.DateTimeField('发布时间', auto_now_add=True)

    def __str__(self):
        return self.title + self.intro
