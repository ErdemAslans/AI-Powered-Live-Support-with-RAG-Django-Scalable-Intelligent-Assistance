from django.urls import path
from .views import create_blog, blog_detail, blog_list

app_name = 'blog'

urlpatterns = [
    path('',blog_list,name='blog_list'),
    path('create/',create_blog,name='create_blog'),
    path('<slug:blog_slug>/',blog_detail,name='blog_detail')
]
