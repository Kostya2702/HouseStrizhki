from django.shortcuts import render, redirect
from .models import Address, Atmosfere, Services
from .forms import ServicesForm
from .models import About


def index(request):
    numbers = Address.objects.all()
    addresses = Address.objects.all()
    add_photo = Atmosfere.objects.all()
    opisanie = About.objects.all()
    prices = Services.objects.all()
    return render(request, 'mainapp/index.html', {'title': 'HouseStrizhki', 
                                                'prices': prices, 
                                                'opisanie': opisanie, 
                                                'add_photo': add_photo,
                                                'addresses': addresses,
                                                'numbers': numbers,
                                                })

def about(request):
    return render(request, 'mainapp/index.html')

def create(request):
    if request.method == 'POST':
        form = ServicesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Неверная форма"

    form = ServicesForm()
    context = {
        "form": form
    }
    return render(request, 'mainapp/create.html', context)

