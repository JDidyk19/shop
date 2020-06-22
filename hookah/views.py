from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Brand_Hookah, Hookah
from .forms import ReviewHookahForm
# Create your views here.

class BrandHookah:
    def get_brand_hookah(self):
        return Brand_Hookah.objects.all()

class FilterBrandHookahView(BrandHookah, ListView):
    template_name = 'hookah/hookah.html'
    def get_queryset(self):
        queryset = Hookah.objects.filter(
            brand__in=self.request.GET.getlist('brand')
        )
        return queryset

class HookahView(BrandHookah, ListView):
    model = Hookah
    queryset = Hookah.objects.all()
    context_object_name = 'hookah_list'
    template_name = 'hookah/hookah.html'

class HookahDetailView(BrandHookah, DetailView):
    model = Hookah
    slug_field = 'slug'
    context_object_name = 'hookah_detail'
    template_name = 'hookah/hookah_detail.html'

class AddHookahReview(View):
    def post(self, request, pk):
        form = ReviewHookahForm(request.POST)
        hookah = Hookah.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.hookah = hookah
            form.save()
        return redirect(hookah.get_absolute_url())

class Search(ListView):
    """ Пошук """
    template_name = 'hookah/hookah.html'
    def get_queryset(self):
        return Hookah.objects.filter(name__icontains=self.request.GET.get('q'))
