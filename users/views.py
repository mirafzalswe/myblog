from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegister
from .models import Post

def regsiter(request):
    if request.method == "POST":
        form = UserRegister(request.POST) # malumtolarni serverga yuklash uchun ihslatiladi
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f" {username} muvofaqiyali royxatdan otingiz")
            return redirect('blog-home')
    else:
        form = UserRegister()
    return render(request, 'users/register.html', {'form':form})