from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from apps.contact.models import Translate
from modeltranslation.admin import TranslationAdmin


# Register your models here.


class TranslationAdminInline(TranslationAdmin):
    model = Translate
    extra = 1 
    
    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            ('Русская версия', {
                'fields': ('title_ru', 'hotline_ru', 'our_location_ru','email_ru'),
            }),
            ('Кыргызская вресия', {
                'fields': ('title_ky', 'hotline_ky', 'our_location_ky','email_ky'),
            }),
        )
        return fieldsets
    
admin.site.register(Translate, TranslationAdminInline)
