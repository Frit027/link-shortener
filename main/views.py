from django.shortcuts import render, redirect
from shortener.models import URL
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return render(request, 'main/index.html')


def check_short_url(request):
    try:
        return redirect(URL.objects.get(token=request.path[1:-1]).long_url)
    except ObjectDoesNotExist:
        return render(request, 'main/index.html')
