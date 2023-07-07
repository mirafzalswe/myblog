from django.shortcuts import render
from users.models import Post
from django.views.generic.list import ListView
# #
# def home(request):
#     # postlar = Post.objects.all()
#     return render(request, 'blog/home.html')

class Home(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'


def about(request):
    return render(request, 'blog/about.html')