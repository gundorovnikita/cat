from django.shortcuts import render
from .models import Post, Categories
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    category = Categories.objects.all()
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context= {
        'contacts':contacts,
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
    paginator = Paginator(pages, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context= {
        'category':category,
        'contacts':contacts,
    }
    return render(request, 'blog/category.html' , context)
