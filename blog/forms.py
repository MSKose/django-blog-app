from .models import Comment, Post
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
       model = Comment
       fields = ('body',)

class PostUpdateForm(forms.ModelForm): 
    class Meta:
        model = Post 
        fields = ['title', 'content', 'post_image'] 