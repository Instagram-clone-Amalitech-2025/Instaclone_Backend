from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    post_count = serializers.IntegerField(read_only=True)
    followers_count = serializers.IntegerField(read_only=True)
    following_count = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)

    class Meta:
        model = Profile
        fields = ['username', 'profile_picture', 'full_name', 'bio', 'website', 'is_private',
                  'post_count', 'followers_count', 'following_count',]
    
    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.user.following.count()
   
    
    