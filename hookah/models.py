from django.db import models
from django.urls import reverse

from product.models import Product
# Create your models here.

""" Бренд каль'янів """
class Brand_Hookah(models.Model):
    name = models.CharField('Назва', max_length=150)
    slug = models.SlugField('URL(Силка)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренди'

""" Каль'яни продукт """
y_n = (
    ('Y', 'Наявний'),
    ('N', 'Відсутній')
)

class Hookah(Product):
    brand = models.ForeignKey(Brand_Hookah,verbose_name='Бренд', on_delete=models.CASCADE, default=True)
    length_hookah = models.PositiveIntegerField("Довжина каль'яну")
    material = models.CharField('Матеріал', max_length=100)
    diametr_hookah_mine = models.FloatField("Діаметр шахти")
    volume_flask = models.FloatField("Об'єм колби")
    conectors = models.IntegerField("Кількість конекторів")
    color_mine = models.CharField("Колір шахти каль'яну", max_length=150)
    color_flask = models.CharField("Колір колби каль'яну", max_length=150)
    diffuser = models.CharField('Дифузор', max_length=10, choices=y_n, default=False)

    def __str__(self):
        return f'{self.brand} {self.name}'

    def get_absolute_url(self):
        return reverse('hookah_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Каль'ян"
        verbose_name_plural = "Каль'яни"

''' Фото каль'янів '''
class PhotosHookah(models.Model):
    title = models.CharField('Заголовок', max_length=150, help_text='Пишіть назву товару')
    image = models.ImageField('Зображення', upload_to='hookah_photos/')
    hookah = models.ForeignKey(Hookah, verbose_name="Каль'ян", on_delete=models.CASCADE, default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фотографія Каль'яну"
        verbose_name_plural = "Фотографії Каль'янів"


'''  Відгуки '''
class ReviewsHookah(models.Model):
    name = models.CharField("Ім'я", max_length=150)
    text = models.TextField('Текст', max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name='Батько', on_delete=models.SET_NULL, blank=True, null=True
    )
    hookah = models.ForeignKey(Hookah, verbose_name="Каль'ян", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.hookah}'

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"