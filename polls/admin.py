from django.contrib import admin
from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'created', 'is_active', 'author')
    fieldsets = [
        (None, { 'fields': [('question_text','created', 'is_active', 'author')] } ),
    ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
