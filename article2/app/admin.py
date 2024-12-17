from django.contrib import admin
from .models import Article
# Register your models here.
admin.site.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display=['name','description']