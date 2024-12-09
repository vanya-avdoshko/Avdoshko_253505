from django.contrib.auth.decorators import user_passes_test, login_required
import requests
from django.shortcuts import render



@login_required
def fact_cat(request):
    url = 'https://catfact.ninja/facts'
    response = requests.get(url)
    data = response.json()
    facts = data['data']
    return render(request, 'core/facts.html', {'data' : facts})