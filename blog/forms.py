from django import forms
from .models import Comment, Post
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class CreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('category','user','text','slug','title','image',)