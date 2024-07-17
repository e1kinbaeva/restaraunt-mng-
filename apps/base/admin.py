from django.contrib import admin
from apps.base.models import Base,Popular_category,Our_chef,News, Our_advantages,Specialmenu_foods,Specialmenu_deserts,Specialmenu_seafood,Specialmenu_beverage
from modeltranslation.admin import TranslationAdmin
# Register your models here.

admin.site.register(Base)
admin.site.register(Popular_category)
admin.site.register(Our_chef)
admin.site.register(News)
admin.site.register(Specialmenu_deserts)
admin.site.register(Specialmenu_seafood)
admin.site.register(Specialmenu_beverage)

class Our_advantagesTranslationAdmin(TranslationAdmin):
    list_display = ('title', 'description')
    model = Our_advantages
    
    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            ('Русская версия', {
                'fields': ('title_ru', 'description_ru'),
            }),
            ('Кыргызская вресия', {
                'fields': ('title_ky', 'description_ky'),
            }),
        )
        return fieldsets

admin.site.register(Our_advantages,Our_advantagesTranslationAdmin)


@admin.register(Specialmenu_foods)
class SpecialMenuAdmin(admin.ModelAdmin):
    list_display = ('name',  'price')
    search_fields = ('name', 'description')







