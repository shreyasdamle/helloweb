from django.shortcuts import render
from collection.models import Cryptocurrency

# Create your views here.
def index(request):
    cryptocurrencys = Cryptocurrency.objects.all()

    return render(request, 'index.html', {
        'cryptocurrencys': cryptocurrencys,
    })

# our new view
def cryptocurrency_detail(request, slug):
    # grab the object...
    cryptocurrency = Cryptocurrency.objects.get(slug=slug)

    # and pass to the template
    return render(request, 'cryptocurrencys/cryptocurrency_detail.html',{
        'cryptocurrency': cryptocurrency,
    })
