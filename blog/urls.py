from django.urls import path
from .views import (
    about, 
    PostListView, 
    # PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView, 
    like_post,
    blog_detail,
    # CommentView,
    # post_comment
    )


urlpatterns = [
    path('', PostListView.as_view(), name="homepage"),
    # path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/<int:id>/', blog_detail, name="post-detail"),
    path('post/create/', PostCreateView.as_view(), name="post-create"),  # PostCreateView by default expects a template named post_form.html (<model>_form.html)
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"), # PostDeleteView by default expects a template named post_confirm_delete.html (<model>_confirm_delete.html)
    path('like/<int:id>', like_post, name='like_post'),
    # path('comment/<int:pk>/', CommentView.as_view(template_name="blog/post_comment"), name="post_comment"),
    # path('comment/<int:id>', post_comment, name='post_comment'),
    path('about/', about, name="about"),
]

