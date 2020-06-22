from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HookahView.as_view(), name = 'hookah'),
    path('brand_hookah/', views.FilterBrandHookahView.as_view(), name='filter_hookah'),
    path('search/', views.Search.as_view(), name='search_hookah'),
    path('<slug:slug>/', views.HookahDetailView.as_view(), name='hookah_detail'),
    path('review-hookah/<int:pk>/', views.AddHookahReview.as_view(), name = 'add_hookah_review'),
]