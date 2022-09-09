from django.shortcuts import render
from .models import Post

# LoginRequiredMixin is simply the class based version for login_required decorator.
# because we cannot use decorators with classes, we are using mixins instead.
# UserPassesTestMixin mixin is for making sure that only the author can edit the posts
from django.contrib.auth.mixins import (LoginRequiredMixin, 
    UserPassesTestMixin)
from django.views.generic import (ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView)



#! FBV for listing blog posts
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

#! CBV for listing blog posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # if I had left this field empty, django would have looked for 'blog/post_list' template cuz it looks for <app>/<model>_<viewtype.html>
    context_object_name = 'posts' # by default django uses the name "object_list". Had this field left empty, I'd have to use object_list to loop through my posts in home.html
    ordering = ['-date_posted']

#! CBV for individual blog posts
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    # actually, for this one lets create the defualt html template file django is looking for. And since this 
    # is a detailview, django's gonna look for a template named 'blog/post_detail.html'. 
    # not defining our context_object_name, we'll have to use 'object' for every post in our blog/post_detail.html template

    
    def get_object(self):
        views = super().get_object()
        views.blog_view += 1
        views.save()
        return views

#! CBV for creating blog posts
class PostCreateView(LoginRequiredMixin, CreateView): # make sure you add your mixins to the left. They should be inherited first, in other words
    model = Post
    fields = ('title', 'content')

    # we are getting an "NOT NULL constraint failed: blog_post.author_id" after posting a blog post which
    # means that the post needs an author and django by default cannot know who the author is. Therfore,
    # we'll need to ovveride the form_valid method and set the author before saving it
    def form_valid(self, form):     
        form.instance.author = self.request.user
        return super().form_valid(form)

#! CBV for updating blog posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Post
    fields = ('title', 'content')

    def form_valid(self, form):     
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): # UserPassesTestMixin requires to override the test_func, thus we are defining it here
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#! CBV for deleting blog posts
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = Post
    # fields = ('title', 'content')
    success_url = '/'

    def test_func(self): 
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html')