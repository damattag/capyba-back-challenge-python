from rest_framework import serializers
from posts import models


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'
