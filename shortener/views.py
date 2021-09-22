from django.shortcuts import render
from datetime import date, timedelta
from hashids import Hashids
from .forms import URLForm


# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver


def shortener_index(request):
    token = ''
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            length = request.POST.get('url_length', 5)
            long_url = form.cleaned_data['long_url']
            url.token = Hashids(salt=long_url, min_length=length).encode(len(long_url))
            token = url.token
            url.expiry_at = date.today() + timedelta(days=7)
            url.save()

    return render(request, 'shortener/shortener_index.html', {'token': token, 'form': URLForm()})
