from django.db import models
from django.urls import reverse

from product.models import Product
# Create your models here.

''' Бренд Табаку '''
class Brand_Tabacco(models.Model):
    name = models.CharField('Назва', max_length=150)
    slug = models.SlugField('URL(Силка)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренди'

""" Табак Продукт """
grams = (
    ('20 gr', '20 грам'),
    ('40 gr', '40 грам'),
    ('50 gr', '50 грам'),
    ('60 gr', '60 грам'),
    ('100 gr', '100 грам'),
    ('125 gr', '125 грам'),
    ('200 gr', '200 грам'),
    ('250 gr', '250 грам'),
    ('1000 gr', '1 кг'),
)

smokyes = (
    ('Н', 'Низька'),
    ('С', 'Середня'),
    ('В', 'Висока')
)

toughneses = (
    ('Л', 'Легкий'),
    ('С', 'Середній'),
    ('В', 'Важкий')
)

heates = (
    ('Н', 'Низька'),
    ('С', 'Середня'),
    ('В', 'Висока')
)

class Tabacco(Product):
    brand = models.ForeignKey(Brand_Tabacco, verbose_name='Бренд', on_delete=models.CASCADE, default=True)
    gram = models.CharField('Грами', max_length=10, choices=grams, default=True)
    tasty = models.CharField('Смак', max_length=150)
    smoky = models.CharField('Димність', max_length=10, choices=smokyes, default=False)
    toughnes = models.CharField('Міцність', max_length=10, choices=toughneses, default=False)
    heat = models.CharField('Жаростійкість', max_length=10, choices=heates, default=False)

    def __str__(self):
        return f'{self.brand} {self.name}'

    def get_absolute_url(self):
        return reverse('tabacco_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Табак"
        verbose_name_plural = "Табаки"

''' Фото табаку '''
class PhotosTabacco(models.Model):
    title = models.CharField('Заголовок', max_length=150, help_text='Пишіть назву товару')
    image = models.ImageField('Зображення', upload_to='hookah_photos/')
    tabacco = models.ForeignKey(Tabacco, verbose_name="Табак", on_delete=models.CASCADE, default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фотографія Табаку"
        verbose_name_plural = "Фотографії Табаків"

''' Відгуки '''
class ReviewsTabacco(models.Model):
    name = models.CharField("Ім'я", max_length=150)
    text = models.TextField('Текст', max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name='Батько', on_delete=models.SET_NULL, blank=True, null=True
    )
    tabacco = models.ForeignKey(Tabacco, verbose_name="Табак", on_delete=models.CASCADE )

    def __str__(self):
        return f'{self.name} {self.tabacco}'

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"
