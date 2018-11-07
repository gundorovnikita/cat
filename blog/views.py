from django.shortcuts import render
from .models import Post
# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    context= {
        'posts':posts,
    }
    return render(request, 'blog/index.html', context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    context= {
        'post':post
    }
    return render(request, 'blog/detail.html' , context)
