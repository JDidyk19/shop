from django.contrib import admin
from .models import Category, Product
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image', 'availabity')
    list_filter = ('name', 'category')
    search_fields = ('name', 'category__name')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width = "100" height = "110"')

    get_image.short_description = 'Постер'
''' 
 superuser:
 login: admin
 password: 1111
'''

admin.site.site_title = 'PeMaGaMa адмінка'
admin.site.site_header = 'PeMaGaMa адмінка'