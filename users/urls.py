from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# tepadagi auth_views bu django vstroin Login va Logaut qiladigna class larini olib kelish

urlpatterns = [
    path('signup/', views.regsiter, name='user-regsiter'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), #bu yerdagi as_view() korinish orqali qilishimz kerak
    # va uni ichiga biz shabloni kiritb ketishimz kerak
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
]