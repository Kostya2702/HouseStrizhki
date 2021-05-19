from django.shortcuts import render, redirect
from .models import Atmosfere, Services
from .forms import ServicesForm
from .models import About


def index(request):
    add_photo = Atmosfere.objects.all()
    opisanie = About.objects.all()
    tasks = Services.objects.all()
    return render(request, 'mainapp/index.html', {'title': 'HouseStrizhki', 'tasks': tasks, 'opisanie': opisanie, 'add_photo': add_photo})

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

