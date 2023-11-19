from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from posts.api import serializers
from posts import models


class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostsSerializer
    queryset = models.Post.objects.all()
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['published']
    search_fields = ['title', 'content']
    ordering_fields = '__all__'
    ordering = ['created_at']


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UsersSerializer
    queryset = models.User.objects.all()


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentsSerializer
    queryset = models.Comment.objects.all()
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['edited']
    search_fields = ['content']
    ordering_fields = '__all__'
    ordering = ['created_at']
