from django.urls import path
from .views import home, about, PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name="homepage"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('about/', about, name="about"),
]

