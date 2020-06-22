from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TabaccoView.as_view(), name = 'tabacco'),
    path('brand_tabacco/', views.FilterBrandTabaccoView.as_view(), name='filter_tabacco'),
    path('search/', views.Search.as_view(), name='search_tabacco'),
    path('<slug:slug>/', views.TabaccoDetailView.as_view(), name='tabacco_detail'),
    path('review-tabacco/<int:pk>/', views.AddTabaccoReview.as_view(), name='add_tabacco_review'),
]