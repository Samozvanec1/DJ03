from django.urls import path

from . import views

urlpatterns = [
    path('', views.Vyvod, name='movies'),
    path('vvod/', views.Vvod, name='home'),

]
