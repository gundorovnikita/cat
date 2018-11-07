from django.urls import path
from django.conf.urls import url
from .views import *
from .models import *

urlpatterns = [
    path('', posts_list, name='posts_list_url') ,
    path('<str:slug>', post_detail, name='post_detail_url')
]
