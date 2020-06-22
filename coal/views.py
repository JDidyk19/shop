from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Coal, ReviewsCoal
from .forms import ReviewCoalForm

# Create your views here.

class CoalView(ListView):
    model = Coal
    context_object_name = 'coal_list'
    template_name = 'coal/coal.html'

class CoalDetailView(DetailView):
    model = Coal
    slug_field = 'slug'
    context_object_name = 'coal_detail'
    template_name = 'coal/coal_detail.html'

class AddCoalReview(View):
    def post(self, request, pk):
        form = ReviewCoalForm(request.POST)
        coal = Coal.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.coal = coal
            form.save()
        return redirect(coal.get_absolute_url())


class Search(ListView):
    """ Пошук """
    template_name = 'coal/coal.html'
    def get_queryset(self):
        return Coal.objects.filter(name__icontains=self.request.GET.get('q'))