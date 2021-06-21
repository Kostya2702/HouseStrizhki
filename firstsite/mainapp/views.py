from mainapp.forms import NoteForm
from django.shortcuts import render
from .models import Address, Atmosfere, Services, Hairdressers, Maps
from .models import About


def index(request):
    numbers = Address.objects.all()
    addresses = Address.objects.all()
    add_photo = Atmosfere.objects.all()
    opisanie = About.objects.all()
    prices = Services.objects.all()
    masters = Hairdressers.objects.all()
    maps = Maps.objects.all()
    notes = NoteForm()
    # p_num = PhoneField() 
    return render(request, 'mainapp/index.html', {'title': 'HouseStrizhki', 
                                                'prices': prices, 
                                                'opisanie': opisanie, 
                                                'add_photo': add_photo,
                                                'addresses': addresses,
                                                'numbers': numbers,
                                                'masters': masters,
                                                'maps': maps,
                                                'notes': notes,
                                                # 'p_num': p_num,
                                                })

def about(request):
    return render(request, 'mainapp/index.html')

def create(request):
    return render(request, 'mainapp/create.html')

