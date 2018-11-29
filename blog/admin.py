from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


class SomeModelAdmin(SummernoteModelAdmin, admin.ModelAdmin):
        summernote_fields = '__all__'
        list_display = ('title','category', 'slug', 'date')


# Register your models here.
admin.site.register(Post, SomeModelAdmin)
admin.site.register(Categories)
admin.site.register(Comment)
