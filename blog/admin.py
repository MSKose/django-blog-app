from django.contrib import admin
from .models import Post, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)

# class PostAdmin(admin.ModelAdmin):
#     model = Post
#     fields = ['title', 'content', 'likes']

# admin.site.register(Post, PostAdmin)
