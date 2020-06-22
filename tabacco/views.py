from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Brand_Tabacco, Tabacco, ReviewsTabacco
from  .forms import ReviewTabaccoForm
# Create your views here.

class BrandTabacco:
    def get_brand_tabacco(self):
        return Brand_Tabacco.objects.all()

class FilterBrandTabaccoView(BrandTabacco, ListView):
    template_name = 'tabacco/tabacco.html'
    def get_queryset(self):
        queryset = Tabacco.objects.filter(
            brand__in=self.request.GET.getlist('brand')
        )
        return queryset

class TabaccoView(BrandTabacco, ListView):
    model = Tabacco
    queryset = Tabacco.objects.all()
    context_object_name = 'tabacco_list'
    template_name = 'tabacco/tabacco.html'

class TabaccoDetailView(BrandTabacco,DetailView):
    model = Tabacco
    slug_field = 'slug'
    context_object_name = 'tabacco_detail'
    template_name = 'tabacco/tabacco_detail.html'

class AddTabaccoReview(View):
    def post(self, request, pk):
        form = ReviewTabaccoForm(request.POST)
        tabacco = Tabacco.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.tabacco = tabacco
            form.save()
        return redirect(tabacco.get_absolute_url())

class Search(ListView):
    """ Пошук """
    template_name = 'tabacco/tabacco.html'
    def get_queryset(self):
        return Tabacco.objects.filter(name__icontains=self.request.GET.get('q'))