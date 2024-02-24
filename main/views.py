from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    data = {
        'title': 'Home',
        'content': 'Main page store',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': False
    }
    return render(request, 'main/index.html', data)


def about(request):
    return HttpResponse("About page")
