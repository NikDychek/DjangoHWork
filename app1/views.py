from django.shortcuts import render, get_object_or_404
from .models import Post


# def index(request):
#     return HttpResponse("Привет, это индексная страница первого приложения!")
#
#
# def page2(request):
#     return HttpResponse("Привет, это вторая страница первого приложения!")

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
