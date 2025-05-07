from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # shows username, but user can't set it

    class Meta:
        model = Post
        fields = ['id', 'user', 'image', 'caption', 'created_at']
