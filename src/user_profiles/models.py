from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    full_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(max_length=300, blank=True)
    website = models.URLField(blank=True)
    is_private = models.BooleanField(default=False)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followed_by', blank=True)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='follows', blank=True)
    last_active = models.DateTimeField(null=True, blank=True)  # Optional

    def post_count(self):
        return self.user.posts.count()

    def followers_count(self):
        return self.followers.count()

    def following_count(self):
        return self.following.count()

    def __str__(self):
        return self.user.username
    
    def follow(self, target_user):
        """Follow another user and update both sides."""
        if target_user != self.user:
            self.following.add(target_user)
            target_profile = Profile.objects.get(user=target_user)
            target_profile.followers.add(self.user)

    def unfollow(self, target_user):
        """Unfollow a user and update both sides."""
        if target_user != self.user:
            self.following.remove(target_user)
            target_profile = Profile.objects.get(user=target_user)
            target_profile.followers.remove(self.user)

    def is_following(self, target_user):
        """Check if self is following target_user."""
        return self.following.filter(id=target_user.id).exists()

    def is_followed_by(self, target_user):
        """Check if self is followed by target_user."""
        return self.followers.filter(id=target_user.id).exists()