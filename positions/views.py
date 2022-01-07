from django.shortcuts import render
import requests
from django.http import HttpResponse
from .models import Position

# Create your views here.
def home(request=None):
    # url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=INR&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    # data = requests.get(url).json()
    # return HttpResponse(data)

    data = Position.objects.all()

    context = {'data': data}
    print(data)
    
    # return render(request, 'positions/main.html')
    return render(request, 'positions/main.html', context)
