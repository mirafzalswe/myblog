from django.shortcuts import render
from users.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

class Home(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
   # ordering =  bu saralaydi oziga qarab vaxtmi joy shunga oxshash

class PostDetail(DetailView):
    model = Post

class CreatePost(CreateView):
    model = Post
    fields = ['title', 'content']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # success_url = 'blog-home'

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog-home')


def about(request):
    return render(request, 'blog/about.html')


