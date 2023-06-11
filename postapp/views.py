from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from .forms import PostForm
from .models import Post, Comment, comment_max_length
from django.contrib.auth.mixins import LoginRequiredMixin

class MainPageView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context


class CreatePageView(LoginRequiredMixin, View):
    def get(self, request):
        post_form = PostForm()
        return render(request, "create.html", context={'form': post_form})

    def post(self, request):
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            title = post_form.cleaned_data['title']
            content = post_form.cleaned_data['content']
            post = Post(title=title, content=content, author=request.user)
            post.save()
            return redirect(f'/post/{title}')
        return render(request, "create.html", context={'form': post_form})

def post_view(request, title):
    post = Post.objects.get(title=title)
    return render(request, "post.html", {'post': post})

def comment_view(request, post_title):
    content = request.POST.get("content")
    if len(content) < comment_max_length:
        post = Post.objects.get(title=post_title)
        comment = Comment(content=content, author=request.user)
        comment.save()
        post.comments.add(comment)
        post.save()
        return redirect(f'/post/{post_title}')
