from django.contrib import admin
from .models import Article, Tags, Category

# Register your models here.

admin.site.register(Tags)
admin.site.register(Article)
admin.site.register(Category)
