from django import forms
from . import models

class PostForm(forms.Form):
    title = forms.CharField(label="Title", max_length=models.title_max_length)
    content = forms.CharField(label="Content", max_length=models.content_max_length, widget=forms.Textarea)

