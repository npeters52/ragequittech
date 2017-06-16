from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'is_archived', 'pub_date', 'author', 'content', 'image')
    fieldsets = [
        (None, { 'fields': [('title', 'is_published', 'is_archived', 'pub_date', 'author', 'content', 'image')] } ),
    ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)