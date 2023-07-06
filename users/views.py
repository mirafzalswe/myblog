from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def regsiter(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) # malumtolarni serverga yuklash uchun ihslatiladi
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f" {username} muvofaqiyali royxatdan otingiz")
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})