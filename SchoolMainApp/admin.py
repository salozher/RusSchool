from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Page, News, Teacher, Subject

@admin.register(Page)
class PageAdmin(TranslationAdmin):
    pass

@admin.register(News)
class NewsAdmin(TranslationAdmin):
    pass

@admin.register(Subject)
class SubjectAdmin(TranslationAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(TranslationAdmin, admin.ModelAdmin):  # Combined inheritance
    list_display = ('first_name', 'last_name', 'middle_name', 'email', 'photo_preview')

    def photo_preview(self, obj):
        from django.utils.html import format_html
        if obj.photo:
            return format_html(f'<img src="{obj.photo.url}" width="50" height="50" />')
        return "No Photo"

    photo_preview.short_description = 'Photo'
