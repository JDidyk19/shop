from django.db import models
from django.urls import reverse
from product.models import Product
# Create your models here.

class Coal(Product):
    material = models.CharField('Вид', max_length=150)
    weith = models.PositiveIntegerField('Вага')
    size = models.FloatField('Розмір')
    producer = models.CharField('Виробник', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вугілля"
        verbose_name_plural = "Вугілля"

    def get_absolute_url(self):
        return reverse('coal_detail', kwargs={'slug': self.slug})


class ReviewsCoal(models.Model):
    name = models.CharField("Ім'я", max_length=150)
    text = models.TextField('Текст', max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name='Батько', on_delete=models.SET_NULL, blank=True, null=True
    )
    coal = models.ForeignKey(Coal, verbose_name="Вугілля", on_delete=models.CASCADE )

    def __str__(self):
        return f'{self.name} {self.coal}'