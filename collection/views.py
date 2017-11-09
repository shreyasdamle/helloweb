from django.shortcuts import render, redirect
from collection.models import Cryptocurrency
from collection.forms import CryptocurrencyForm



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

def edit_cryptocurrency(request, slug):
    # grab the object
    cryptocurrency = Cryptocurrency.objects.get(slug=slug)
    # set the form we're using
    form_class = CryptocurrencyForm

    # if we're coming to this view from a submitted form
    if request.method == 'POST':
        # grab the data from the submitted form and apply to
        # the form
        form = form_class(data=request.POST, instance=cryptocurrency)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('cryptocurrency_detail', slug=cryptocurrency.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=cryptocurrency)

    # and render the template
    return render(request, 'cryptocurrencys/edit_cryptocurrency.html', {
        'cryptocurrency': cryptocurrency,
        'form': form,
    })
