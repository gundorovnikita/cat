from django import forms
from .models import Comment, Post, Categories
from django.contrib.auth.models import User
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class CreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('category','text','slug','title','image',)

class CreateCategory(forms.ModelForm):
    class Meta:
        model = Categories
        fields =('name','slug',)

class UserLoginForm(forms.Form):
    username = forms.CharField(label='')
    password = forms.CharField(label='', widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Enter Password Here...'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Confirm Password...'}))
    class Meta:
        model = User
        fields = {
            'username',
            'email',
        }
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise form.ValidationError('Password Mismatch')
        return confirm_password    
