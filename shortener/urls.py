from . import views
from django.urls import path


urlpatterns = [
    path('', views.shortener_index, name='shortener')
]
