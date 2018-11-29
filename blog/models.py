from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def get_absolute_url(self):
        return reverse('categories_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name



class Post(models.Model):
    category = models.ForeignKey('Categories', on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField('Текст статьи', null=True,blank=True)
    slug = models.SlugField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL,null=True)
    text = models.TextField(max_length=180)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text
