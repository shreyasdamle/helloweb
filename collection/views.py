from django.shortcuts import render

# Create your views here.
def index(request):
    # defining the variable
    number = 7478.24
    # passing the variable to the view
    thing = "Bitcoin"
    return render(request, 'index.html', {
        'number': number,
        'thing': thing,
    })
