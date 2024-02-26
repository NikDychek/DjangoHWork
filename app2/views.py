from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Привет, это индексная страница второго приложения!")

def page2(request):
    return HttpResponse("Привет, это вторая страница второго приложения!")