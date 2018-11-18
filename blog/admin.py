from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

class SomeModelAdmin(SummernoteModelAdmin):
        summernote_fields = '__all__'

# Register your models here.
admin.site.register(Post, SomeModelAdmin)
admin.site.register(Categories)
