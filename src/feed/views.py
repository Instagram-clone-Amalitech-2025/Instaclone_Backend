from rest_framework import generics, permissions
from .models import Post, Follow
from .serializers import PostSerializer

class FeedView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        followed_user_ids = Follow.objects.filter(follower=user).values_list('following_id', flat=True)
        # Include the user's own posts in the feed
        return Post.objects.filter(user_id__in=list(followed_user_ids) + [user.id]).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)