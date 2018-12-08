from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Post, Categories, Comment
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import datetime
from django.utils import timezone


def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    category = Categories.objects.all()
    count = Post.objects.all().count()
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context= {
        'count':count,
        'contacts':contacts,
        'category':category,
    }
    return render(request, 'blog/index.html', context)

def posts_list_likes(request):
    posts = Post.objects.all().order_by('-likes')
    category = Categories.objects.all()
    count = Post.objects.all().count()
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context= {
        'count':count,
        'contacts':contacts,
        'category':category,
    }
    return render(request, 'blog/index.html', context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post).order_by('-timestamp')
    total = Comment.objects.filter(post=post).count()
    paginator = Paginator(comments, 6)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    comment_form=CommentForm()
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            text = request.POST.get('text')
            text = Comment.objects.create(post=post, text=text, user=request.user)
            text.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()

    context= {
        'total':total,
        'post':post,
        'comment_form': comment_form,
        'contacts': contacts,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
    }
    return render(request, 'blog/detail.html' , context)

def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(post.get_absolute_url())



def Categories_detail(request, slug):
    category = Categories.objects.get(slug=slug)
    pages = Post.objects.filter(category=category).order_by('-date')
    count = Post.objects.filter(category=category).count()
    paginator = Paginator(pages, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context= {
        'category':category,
        'contacts':contacts,
        'count':count,
    }
    return render(request, 'blog/category.html' , context)

def post_random(request):
    posts = Post.objects.all().order_by('?')[:1]
    context= {
        'posts': posts,
    }
    return render(request, 'blog/random.html', context)

def post_create(request):
    if request.method == 'POST':
        create = CreateForm(request.POST, request.FILES)
        if create.is_valid():
            post = create.save(commit=False)
            post.user = request.user
            post.date = timezone.now()
            post.save()
            return redirect('http://localtest.me:8000/posts')
    else:
        create = CreateForm()
    context= {
        'create': create,
    }
    return render(request, 'blog/create.html', context)

def category_create(request):
    if request.method == 'POST':
        create = CreateCategory(request.POST)
        if create.is_valid():
            name = create.save(commit=False)
            name.save()
            return redirect('http://localtest.me:8000/posts/create')
    else:
        create = CreateCategory()
    context= {
        'create': create,
    }
    return render(request, 'blog/create_category.html', context)

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('posts_list_url'))
                else:
                    return HttpResponseRedirect('User is not active')
            else:
                return HttpResponse('User is None')
    else:
        form = UserLoginForm()
    context={
        'form':form,
    }
    return render(request, 'blog/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('posts_list_url')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            logout(request)
            return redirect('posts_list_url')
    else:
        form = UserRegistrationForm()
    context = {
        'form':form,
    }
    return render(request,'registration/register.html', context)
