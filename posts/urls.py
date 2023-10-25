from django.urls import path

from posts.api import PostListCreateAPIView

urlpatterns = [
    path("", PostListCreateAPIView.as_view()),
]