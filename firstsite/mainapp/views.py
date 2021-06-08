from django.shortcuts import render
from .models import Address, Atmosfere, Services, Title_for_section
from .models import About


def index(request):
    numbers = Address.objects.all()
    addresses = Address.objects.all()
    add_photo = Atmosfere.objects.all()
    opisanie = About.objects.all()
    prices = Services.objects.all()
    titles = Title_for_section.objects.all()
    return render(request, 'mainapp/index.html', {'title': 'HouseStrizhki', 
                                                'prices': prices, 
                                                'opisanie': opisanie, 
                                                'add_photo': add_photo,
                                                'addresses': addresses,
                                                'numbers': numbers,
                                                'titles': titles,
                                                })

def about(request):
    return render(request, 'mainapp/index.html')

def create(request):
    return render(request, 'mainapp/create.html')

