from . import views
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='home'),
    url(r'^[A-Za-z0-9]{1,7}/$', views.check_short_url)
]
