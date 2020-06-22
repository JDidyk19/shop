from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CoalView.as_view(), name = 'coal'),
    path('search/', views.Search.as_view(), name='search_coal'),
    path('<slug:slug>/', views.CoalDetailView.as_view(), name='coal_detail'),
    path('review-coal/<int:pk>/', views.AddCoalReview.as_view(), name='add_coal_review'),
]