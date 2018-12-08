from django.urls import path
from django.conf.urls import url
from .views import *
from .models import *

urlpatterns = [
    path('', posts_list, name='posts_list_url') ,
    path('create', post_create, name='post_create_url'),
    path('create/category', category_create, name='category_create_url'),
    path('random', post_random, name='post_random_url'),
    path('ind/<str:slug>', post_detail, name='post_detail_url'),
    path('category/<str:slug>', Categories_detail, name='categories_detail_url'),
    path('like', like_post, name='like_post_url'),
    path('sort_by_likes', posts_list_likes, name='posts_likes_url'),
    path('login', user_login, name='user_login_url'),
    path('logout', user_logout, name='user_logout_url'),
    path('register', register, name='register_url'),
]
