from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='blog-home'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('post/new/', views.CreatePost.as_view(), name='new-post'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/update', views.PostUpdate.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.PostDelete.as_view(), name='delete-post')
]