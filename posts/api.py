from posts.models import Post
from rest_framework.generics import CreateAPIView


from .serializers import PostSerializer


from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from users.models import User


class PostListCreateAPIView(CreateAPIView):
    serializer_class = PostSerializer
    lookup_field = "user_id"

    def get_queryset(self):
        user = get_object_or_404(
            User.objects.all(), id=self.kwargs[self.lookup_field]
        )

        if user != self.request.user:
            raise Http404

        posts = Post.objects.filter(user=user)
        
        return posts

    @staticmethod
    def get_posts(user: User):
        """Get posts for current user."""

        posts = Post.objects.filter(user=user)
        return get_object_or_404(posts)

    def post(self, request):
        self.get_posts(request.user)
        payload = {"text": request.data["text"], "user": request.user}
        serializer = self.get_serializer(data=payload)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
