from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField('Категорія', max_length=150)
    poster = models.ImageField('Постер категорії', upload_to='category_poster/')

    def __str__(self):
        return f'{self.id} {self.name}'

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

class Product(models.Model):
    name = models.CharField('Назва', max_length=150)
    slug = models.SlugField('URL(Силка)', help_text='Пишіть бренд товару, потім назву(brand-name)', unique=True)
    category = models.ForeignKey(
        Category, verbose_name='Категорія', on_delete=models.SET_NULL, blank=True, null=True
    )
    description = models.TextField('Опис', blank=True, null=True)
    poster = models.ImageField('Фотка товару', upload_to='product_posters/')
    country = models.CharField('Країна виробника', max_length=150, blank=True, null=True)
    availabity = models.BooleanField('Наявність Товару', default=True, blank=False)
    price = models.PositiveIntegerField("Ціна")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

