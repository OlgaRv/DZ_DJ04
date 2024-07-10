from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm

def home(request):
    return render(request, 'films/home.html')

def add_film(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_films')
    else:
        form = FilmForm()
    return render(request, 'films/add_film.html', {'form': form})

def list_films(request):
    films = Film.objects.all()
    return render(request, 'films/list_films.html', {'films': films})


