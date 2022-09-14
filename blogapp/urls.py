from django.urls import path
from . import views
urlpatterns = [
    path('', views.blog_index, name = 'blog_index'),
    path('article/<slug:slug>', views.blog_detail, name = 'blog_detail'),
    path("like_post", views.like_post, name="like")
]