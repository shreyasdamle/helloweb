from django.shortcuts import render
from collection.models import Cryptocurrency

# Create your views here.
def index(request):
    Cryptocurrencys = Cryptocurrency.objects.all()

    return render(request, 'index.html', {
        'Cryptocurrencys': Cryptocurrencys,
    })
