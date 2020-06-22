from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Category, Product
# Create your views here.

class Index(View):
    def get(self, request):
        hookah_category = Category.objects.get(pk=1)
        tabacco_category = Category.objects.get(pk=2)
        coal_category = Category.objects.get(pk=3)
        accessories_category = Category.objects.get(pk=4)

        context = {
            'hookah_category': hookah_category,
            'tabacco_category': tabacco_category,
            'coal_category': coal_category,
            'accessories_category': accessories_category
        }
        return render(request, 'index.html', context)

class List(ListView):
    model = Product
    queryset = Product.objects.all()






