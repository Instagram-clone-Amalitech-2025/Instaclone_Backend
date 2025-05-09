from django.db import models
from django.conf import settings

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='posts/images/', blank=True, null=True)
    video = models.FileField(upload_to='posts/videos/', blank=True, null=True)
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        if not self.image and not self.video:
            raise ValidationError("Post must have either an image or a video.")
        if self.image and self.video:
            raise ValidationError("Post cannot have both an image and a video.")

    def __str__(self):
        return f"{self.user.username}'s post at {self.created_at}"
