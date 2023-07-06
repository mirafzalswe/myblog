from django.shortcuts import render
from users.models import Post

def home(request):
    postlar = Post.objects.all()
    return render(request, 'blog/home.html',{'postlar':postlar})

def about(request):
    return render(request, 'blog/about.html')