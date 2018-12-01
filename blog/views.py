from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from .models import Post, Categories, Comment
from .forms import CommentForm, CreateForm, CreateCategory
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import datetime
from django.utils import timezone

#if request.method == "POST":
#    comment = Comment(request.POST)
#    return redirect('post_detail_url', slug=post.slug)
#else:
#    comment = Comment()


# Create your views here.

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

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.filter(post=post).order_by('-timestamp')[:10]
    total = Comment.objects.filter(post=post).count()
    comment_form=CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            text = request.POST.get('text')
            text = Comment.objects.create(post=post, text=text)
            text.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()

    context= {
        'total':total,
        'post':post,
        'comments':comments,
        'comment_form': comment_form,
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
            return redirect('http://127.0.0.1:8000/posts/create')
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
            return redirect('http://127.0.0.1:8000/posts/create/category')
    else:
        create = CreateCategory()
    context= {
        'create': create,
    }
    return render(request, 'blog/create_category.html', context)
