from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm


# def index(request):
#     return HttpResponse("Привет, это индексная страница первого приложения!")
#
#
# def page2(request):
#     return HttpResponse("Привет, это вторая страница первого приложения!")

def post_list(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts, 'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
