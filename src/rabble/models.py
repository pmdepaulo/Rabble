from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.IntegerField(primary_key=True)
    username = models.TextField(unique=True)
    first_name = models.TextField(null=True)
    last_name = models.TextField(null=True)
    bio = models.TextField(null=True)
    interests = models.JSONField(default=list)
    email = models.TextField(unique=True)

    def __str__(self):
        return self.username

class User_Followers(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    follower_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')

class Communities(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(unique=True)
    owner_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    admin = models.JSONField(default=list)

class Community_Members(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    community_id = models.ForeignKey(Communities, on_delete=models.CASCADE)

class SubRabbles(models.Model):
    id = models.IntegerField(primary_key=True)
    rabble_name = models.TextField(unique=True)
    display_name = models.TextField(null=True)
    description = models.TextField(null=True)
    community_id = models.ForeignKey(Communities, on_delete=models.CASCADE)
    public = models.BooleanField(default=True)
    allow_anon = models.BooleanField(default=True)

    def __str__(self):
        return self.rabble_name

class SubRabble_Members(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subrabble_id = models.ForeignKey(SubRabbles, on_delete=models.CASCADE)

class SubRabble_Admin(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subrabble_id = models.ForeignKey(SubRabbles, on_delete=models.CASCADE)

class Posts(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(null=True)
    body = models.TextField(null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subrabble_id = models.ForeignKey(SubRabbles, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    anonymous = models.BooleanField(default=False)

class Comments(models.Model):
    id = models.IntegerField(primary_key=True)
    body = models.TextField(null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    anonymous = models.BooleanField(default=False)

class Likes(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Conversations(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    community_id = models.ForeignKey(Communities, on_delete=models.CASCADE)

class Conversation_Members(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation_id = models.ForeignKey(Conversations, on_delete=models.CASCADE)

class Conversation_Messages(models.Model):
    id = models.IntegerField(primary_key=True)
    body = models.TextField(null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation_id = models.ForeignKey(Conversations, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)