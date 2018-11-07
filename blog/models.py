from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey('Categories', on_delete=models.CASCADE,null=True,blank=True)
    slug = models.SlugField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})
