from rest_framework import serializers
from posts import models


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'
