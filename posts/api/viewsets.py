from rest_framework import viewsets
from posts.api import serializers
from posts import models


class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostsSerializer
    queryset = models.Post.objects.all()
