from django.contrib import admin
from django import forms
from .models import Coal, ReviewsCoal
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
# Register your models here.

class CoalAdminForm(forms.ModelForm):
    description = forms.CharField(label='Опис', widget=CKEditorUploadingWidget())
    class Meta:
        model = Coal
        fields = '__all__'

@admin.register(Coal)
class CoalhAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image', 'availabity')
    list_filter = ('name',)
    search_fields = ('name',)
    save_on_top = True
    form = CoalAdminForm
    list_editable = ('availabity',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width = "100" height = "110"')

    get_image.short_description = 'Постер'

    fieldsets = (
        ('Про товар', {
            "fields": (('name', 'slug', 'description', 'availabity', 'category'))
        }),
        ('Фотографія', {
            "fields": ('poster', 'get_image')
        }),
        ('Матеріал', {
            "fields": ('material',)
        }),
        ('Характеристика', {
            "fields": (('weith', 'size'),)
        }),
        ('Виробник', {
            "fields": ('producer',)
        }),
        ('Ціна', {
            # "classes": ('collapse',),
            "fields": ('price',)
        }),
    )