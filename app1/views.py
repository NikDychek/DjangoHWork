from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    return HttpResponse("Привет, это индексная страница первого приложения!")


def page2(request):
    return HttpResponse("Привет, это вторая страница первого приложения!")


# def tab1(request):
#     my_post = Post.objects.get(id=1)
#     return render(request, 'first_post.html', {'my_post': my_post})
#
#
# def tab2(request):
#     return render(request, 'second_post.html')
