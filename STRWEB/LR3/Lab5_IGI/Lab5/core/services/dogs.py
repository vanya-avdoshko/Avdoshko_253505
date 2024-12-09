from django.contrib.auth.decorators import user_passes_test, login_required
import requests
from django.shortcuts import render



@login_required
def dogs(request):
    url = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(url)
    data = response.json()
    image = data['message']
    return render(request, 'core/dogs.html', {'image': image})
