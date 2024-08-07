from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='news'),
    path('create/', views.news_create, name='create'),
]
