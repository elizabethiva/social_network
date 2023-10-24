from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        if user not in post.likes.all():
            post.likes.add(user)
            return Response({'message': 'Liked'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['POST'])
    def unlike(self, request, pk=None):
        post = self.get_object()
        user = request.user
        if user in post.likes.all():
            post.likes.remove(user)
            return Response({'message': 'Unliked'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Not liked yet'}, status=status.HTTP_400_BAD_REQUEST)