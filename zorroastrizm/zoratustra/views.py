from django.shortcuts import render

def index(request):
    data = {'caption': 'Главная страница'}
    return render(request, 'zoratustra/index.html', data)
def about(request):
    data = {'caption': 'О нас'}
    return render(request, 'zoratustra/about.html', data)

def Zara(request):
    return render(request, 'zoratustra/Zara.html')
def neZara(request):
    return render(request, 'zoratustra/neZara.html')


