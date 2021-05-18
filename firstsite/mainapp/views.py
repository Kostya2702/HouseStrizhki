from django.shortcuts import render, redirect
from .models import Services
from .forms import ServicesForm
from .models import About


def index(request):
    opisanie = About.objects.all()
    tasks = Services.objects.order_by('-id')
    return render(request, 'mainapp/index.html', {'title': 'HouseStrizhki', 'tasks': tasks, 'opisanie': opisanie})

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

