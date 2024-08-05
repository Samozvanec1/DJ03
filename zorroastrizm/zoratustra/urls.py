from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about/zoratustra', views.about, name='about'),
    path('about/Zara', views.Zara, name='Zara'),
    path('about/neZara', views.neZara, name='neZara'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)