from modeltranslation.translator import register, TranslationOptions
from .models import Page, News, Teacher, Subject, AgeGroup

@register(Page)
class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')

@register(Teacher)
class TeacherTranslationOptions(TranslationOptions):
    fields = ('first_name', 'middle_name', 'last_name')

@register(Subject)
class SubjectTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'long_description')

@register(AgeGroup)
class AgeGroupTranslationOptions(TranslationOptions):
    fields = ('age_definition',)
