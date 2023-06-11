from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPageView.as_view()),
    path('create', views.CreatePageView.as_view(), name='create'),
    path('post/<str:title>', views.post_view),
    path('comment/<str:post_title>', views.comment_view)
]