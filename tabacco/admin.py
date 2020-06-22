from django.contrib import admin
from django import forms
from .models import Brand_Tabacco, Tabacco, PhotosTabacco
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
# Register your models here.

class TabaccoAdminForm(forms.ModelForm):
    description = forms.CharField(label='Опис', widget=CKEditorUploadingWidget())
    class Meta:
        model = Tabacco
        fields = '__all__'

@admin.register(Brand_Tabacco)
class BrandTabaccoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)

class TabaccoPhotosInline(admin.TabularInline):
    model = PhotosTabacco
    extra = 1
    readonly_fields = ('get_image',)
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width = "100" height = "110"')

    get_image.short_description = 'Зображення'

@admin.register(Tabacco)
class TabaccoAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image', 'availabity')
    list_filter = ('name', 'brand')
    search_fields = ('name',)
    inlines = [TabaccoPhotosInline]
    save_on_top = True
    form = TabaccoAdminForm
    list_editable = ('availabity',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width = "100" height = "110"')

    get_image.short_description = 'Постер'

    fieldsets = (
        ('Про товар', {
            "fields": (('brand', 'name', 'slug', 'description', 'availabity', 'category'))
        }),
        ('Фотографія', {
            "fields": ('poster', 'get_image')
        }),
        ('Смак', {
            "fields": ('tasty',)
        }),
        ('Характеристика', {
            "fields": (('smoky', 'toughnes', 'heat', 'gram'),)
        }),
        ('Країна', {
            "fields": ('country',)
        }),
        ('Ціна', {
            # "classes": ('collapse',),
            "fields": ('price',)
        }),
    )

@admin.register(PhotosTabacco)
class PhotoTabaccoAdmin(admin.ModelAdmin):
    list_display = ('title', 'tabacco', 'get_image')
    list_filter = ('tabacco',)
    search_fields = ('title',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width = "100" height = "110"')

    get_image.short_description = 'Зображення'
