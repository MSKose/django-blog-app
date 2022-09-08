from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# FBV for listing blog posts
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

# CBV for listing blog posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # if I had left this fielt empty, django would have looked for 'blog/post_list' template cuz it looks for <app>/<model>_<viewtype.html>
    context_object_name = 'posts' # by default django uses the name "object_list". Had this field left empty, I'd have to use object_list to loop through my posts in home.html
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    # actually, for this one lets create the defualt html template file django is looking for. And since this 
    # is a detalview, djnago's gonna for a template named 'blog/post_detail.html'. 
    # not naming our context_object_name, we'll have to use object for every post in our blog/post_detail.html template

def about(request):
    return render(request, 'blog/about.html')