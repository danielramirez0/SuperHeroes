from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name = 'superheroes'
urlpatterns = [
    path('index/', views.index, name='index')
]