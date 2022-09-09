from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # since one post can have one author but one author can have multiple posts we use many-to-1 relation
    # since we want to delete the posts related to the author if author is deleted, we use on_delete=models.CASCADE
    # but, notice that the opposite is not true; if a post is deleted author won't be deleted. It is called cascade for a reason
    author = models.ForeignKey(User, on_delete=models.CASCADE) 

    # see here for view reference: https://stackoverflow.com/a/61745605
    blog_view = models.IntegerField(default=0)

    # I mainly followed this article for reload-free like functionality: https://blog.devgenius.io/django-and-htmx-part-1-ff629ae048f1
    likes = models.ManyToManyField(User, blank=True, related_name="collected_votes", null=True)


    def __str__(self):
        return self.title


    # without the following function defined we'd get "No URL to redirect to. Either provide a url or define a get_absolute_url method on the Model."
    # error. Thus, defining a get_absolute_url we make sure that we are directed to "post-detail"
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    