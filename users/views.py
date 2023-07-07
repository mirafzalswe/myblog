from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegister, UpdateProfile, UpdateAvatar
from .models import Post
from django.contrib.auth.decorators import login_required

def regsiter(request):
    if request.method == "POST":
        form = UserRegister(request.POST) # malumtolarni serverga yuklash uchun ihslatiladi
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f" {username} muvofaqiyali royxatdan otingiz")
            return redirect('login')
    else:
        form = UserRegister()
    return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
    if request.method == "POST":
        pic = UpdateAvatar(request.POST, request.FILES, instance=request.user.profile)
        info = UpdateProfile(request.POST, instance=request.user)
        if pic.is_valid() and info.is_valid():
            pic.save()
            info.save()
            messages.success(request, f"ozgarishalr qabul qilindi")
    else:
        pic = UpdateAvatar(instance=request.user.profile)
        info = UpdateProfile(instance=request.user)


    return render(request, 'users/profile.html', {'pic':pic, 'info': info})
