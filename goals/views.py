from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    pageTitle = 'Objetivos'
    return render(request, 'goals/pages/home.html', {'title': pageTitle})

def goals(request, id):
    pageTitle = 'Objetivo - 1'
    return render(request, 'goals/pages/goal-view.html', {'title': pageTitle})