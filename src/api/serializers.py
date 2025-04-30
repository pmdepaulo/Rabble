from rest_framework import serializers
from rabble.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'bio', 'interests', 'email']

class User_FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Followers
        fields = ['user_id', 'follower_id']

class CommunitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communities
        fields = ['id', 'name', 'owner_user_id', 'admin']

class Community_MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Community_Members
        fields = ['user_id', 'community_id']

class SubRabblesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubRabbles
        fields = ['id', 'rabble_name', 'display_name', 'description', 'community_id', 'public', 'allow_anon']

class SubRabble_MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubRabble_Members
        fields = ['user_id', 'subrabble_id']

class SubRabble_AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubRabble_Admin
        fields = ['user_id', 'subrabble_id']

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id', 'title', 'body', 'user_id', 'subrabble_id', 'created_at', 'anonymous']

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'body', 'user_id', 'post_id', 'created_at', 'anonymous']

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = ['user_id', 'post_id', 'created_at']

class ConversationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversations
        fields = ['id', 'owner_user_id', 'community_id', 'created_at', 'updated_at']

class Conversation_MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation_Members
        fields = ['user_id', 'conversation_id']

class Conversation_MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation_Messages
        fields = ['id', 'body', 'user_id', 'conversation_id', 'created_at']