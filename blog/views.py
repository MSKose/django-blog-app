# from urllib import request
from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect


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
    # ordering = ['-date_posted']

#! CBV for individual blog posts
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    form = CommentForm
    # actually, for this one let's create the defualt html template file django is looking for. And since this 
    # is a detailview, django's gonna look for a template named 'blog/post_detail.html'. 
    # not defining our context_object_name, we'll have to use 'object' for every post in our blog/post_detail.html template
    success_url = '/'

    initial = {'key': 'value'}
    template_name = 'blog/post_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})


    #? view count part
    def get_object(self):
        views = super().get_object()
        views.blog_view += 1
        views.save()
        print(CommentForm)
        print(Post.objects.get(id = views.pk) == views)
        # if request.method == 'POST':
        #     print(CommentForm(request.POST))
        # if form.is_valid():
        #     comment=form.save(commit=False)
        #     comment.blog = views
        #     comment.save()

        return views

    def form_valid(self, form):     
        form.instance.author = self.request.user
        return super().form_valid(form)

#! CBV for creating blog posts
class PostCreateView(LoginRequiredMixin, CreateView): # make sure you add your mixins to the left. They should be inherited first, in other words
    model = Post
    fields = ('title', 'content')

    # we are getting a "NOT NULL constraint failed: blog_post.author_id" after posting a blog post which
    # means that the post needs an author and django by default cannot know who the author is. Therefore,
    # we'll need to override the form_valid method and set the author before saving it
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



def like_post(request, id):
    if request.method == "POST":
        instance = Post.objects.get(id=id)
        # print(request.user.id, id)
        # print(instance.author)
        # print(instance.likes.id)
        if not instance.likes.filter(id=request.user.id).exists():
            instance.likes.add(request.user)
            instance.save() 
            # print(instance)
            return render( request, 'blog/likes_area.html', context={'post':instance})
        else:
            instance.likes.remove(request.user)
            instance.save() 
            # print(instance)
            return render( request, 'blog/likes_area.html', context={'post':instance})

# def post_comment(request, id):
#     model = Comment.objects.get(id=id)
#     comment = CommentForm(instance=model)

#     if request.method == "POST":
#         comment = CommentForm(request.POST, instance=model)
#         # instance = CommentForm(request, id=id)
#         if comment.is_valid():
#             comment.save() 
#             return render( request, 'blog/post_comment.html', context={'comment':comment})

# class CommentView(CreateView):
#     model = Comment

#     template_name = 'blog/post_comment.html'

#     fields = ('post', 'body','date_added')

def about(request):
    return render(request, 'blog/about.html')