from django.shortcuts import render
from datetime import date, timedelta
from .forms import URLForm
from .token_creator import TokenCreator
from validators import url as valid_url


# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver


def shortener_index(request):
    form = URLForm(request.POST or None)
    if request.method == 'GET':
        token = 'GET'
    elif form.is_valid():
        long_url = form.cleaned_data['long_url']
        if not valid_url(long_url):
            return render(request, 'shortener/shortener_index.html', {'token': 'URL не корректен!', 'form': form})

        url = form.save(commit=False)

        requested_length = int(request.POST.get('requested_length', 5))
        url.token = token = TokenCreator.get_token(long_url, requested_length)
        url.expiry_at = date.today() + timedelta(days=7)
        url.save()
    else:
        token = 'NOT_VALID'
    return render(request, 'shortener/shortener_index.html', {'token': token, 'form': form})
