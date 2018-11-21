from django.shortcuts import render
from .models import Post, Categories
# Create your views here.

def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    category = Categories.objects.all()
    context= {
        'posts':posts,
        'category':category,
    }
    return render(request, 'blog/index.html', context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    context= {
        'post':post,
    }
    return render(request, 'blog/detail.html' , context)

def Categories_detail(request, slug):
    category = Categories.objects.get(slug=slug)
    pages = Post.objects.filter(category=category).order_by('-date')
    context= {
        'category':category,
        'pages':pages,
    }
    return render(request, 'blog/category.html' , context)
