from django.db import models
import uuid


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    email = models.TextField(unique=True)
    password = models.TextField()
    image = models.TextField(blank=True, null=True)
    accepted_terms = models.BooleanField()
    email_verified = models.BooleanField(default=False)
    email_verification_token = models.TextField(blank=True, null=True)
    email_verification_token_expiry = models.DateTimeField(
        blank=True, null=True)
    role = models.TextField(default='user')


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    author = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='posts')


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    content = models.TextField()

    author = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='comments')

    post = models.ForeignKey(
        'Post', on_delete=models.CASCADE, related_name='comments')

    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='children', null=True)
