from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogHome, name="blogHome"),
    path('<str:slug>', views.blogPost, name="blogPost"),
    path('blog/postComment', views.postComment, name="postComment"),
]