from django.shortcuts import render, redirect
from .forms import FilmForm
from .models import Film

def Vvod(request):
    error = ''
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies')
        else:
            error = 'Ваш фильм баян, давай новенькое'
            return render(request, 'films/Vvod.html', {'form': form, 'error': error})

    form = FilmForm()
    return render(request, 'films/Vvod.html', {'form': form, 'error': error})

def Vyvod(request):
    films = Film.objects.all()
    context = {
        'films': films
    }
    return render(request, 'films/Vyvod.html', context)
