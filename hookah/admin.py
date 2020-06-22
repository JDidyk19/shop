from django.contrib import admin
from django import forms
from .models import Brand_Hookah, Hookah, PhotosHookah
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
# Register your models here.

class HookahAdminForm(forms.ModelForm):
    description = forms.CharField(label='Опис', widget=CKEditorUploadingWidget())
    class Meta:
        model = Hookah
        fields = '__all__'

@admin.register(Brand_Hookah)
class BrandHookahAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)

class HookahPhotosInline(admin.TabularInline):
    model = PhotosHookah
    extra = 1
    readonly_fields = ('get_image',)
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width = "100" height = "110"')

    get_image.short_description = 'Зображення'

@admin.register(Hookah)
class HookahAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image', 'availabity')
    list_filter = ('name', 'brand')
    search_fields = ('name',)
    inlines = [HookahPhotosInline]
    save_on_top = True
    form = HookahAdminForm
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
        ('Матеріал і колір', {
            "fields": (('material', 'color_mine', 'color_flask'),)
        }),
        ('Характеристика', {
            "fields": (('length_hookah', 'diametr_hookah_mine', 'volume_flask', 'conectors', 'diffuser'),)
        }),
        ('Країна', {
            "fields": ('country',)
        }),
        ('Ціна', {
            # "classes": ('collapse',),
            "fields": ('price',)
        }),
    )

@admin.register(PhotosHookah)
class PhotoHookahAdmin(admin.ModelAdmin):
    list_display = ('title', 'hookah', 'get_image')
    list_filter = ('hookah',)
    search_fields = ('title',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width = "100" height = "110"')

    get_image.short_description = 'Зображення'