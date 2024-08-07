from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm

def index(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'news/news.html', context)

def news_create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Ваши новости протухли, несите свежие'
            return render(request, 'news/news_create.html', {'form': form, 'error': error})

    form = NewsForm()
    return render(request, 'news/news_create.html', {'form': form, 'error': error})