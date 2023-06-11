from django.db import models
from django.contrib.auth.models import User

title_max_length: int = 30
content_max_length: int = 2000
comment_max_length: int = 200

class Comment(models.Model):
    content = models.CharField(max_length=comment_max_length)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

class Post(models.Model):
    title = models.CharField(max_length=title_max_length, unique=True, primary_key=True)
    content = models.CharField(max_length=content_max_length)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    comments = models.ManyToManyField(Comment, blank=True, null=True, default=None)

    def __repr__(self):
        return f"title:{self.title}" \
               f"content:{self.content}" \
               f"author:{self.author}" \
               f"created_on:{self.created_on}" \
               f"updated_on:{self.updated_on}"
