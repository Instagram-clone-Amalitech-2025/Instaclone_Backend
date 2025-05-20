from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.user:
            raise PermissionDenied("You cannot edit someone else's profile.")
        serializer.save()

    def perform_create(self, serializer):
        user = self.request.user
        if Profile.objects.filter(user=user).exists():
            raise PermissionDenied("Profile already exists for this user.")
        serializer.save(user=user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def follow(self, request, pk=None):
        profile_to_follow = self.get_object()               
        user_profile = Profile.objects.get(user=request.user)  

        if profile_to_follow.user == request.user:
         return Response({"error": "You cannot follow yourself."}, status=400)

        user_profile.follow(profile_to_follow.user)  

        return Response({"status": f"You are now following {profile_to_follow.user.username}"})


    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unfollow(self, request, pk=None):
        profile_to_unfollow = self.get_object()
        user_profile = Profile.objects.get(user=request.user)

        if profile_to_unfollow.user == request.user:
          return Response({"error": "You cannot unfollow yourself."}, status=400)

        user_profile.unfollow(profile_to_unfollow.user)  

        return Response({"status": f"You have unfollowed {profile_to_unfollow.user.username}"})

    
    @action(detail=True, methods=['get'])
    def followers(self, request, pk=None):
        profile = self.get_object()
        followers = profile.followers.all()
        follower_usernames = [user.username for user in followers]
        return Response({"followers": follower_usernames})
    
    @action(detail=True, methods=['get'])
    def following(self, request, pk=None):
        profile = self.get_object()

  
        following_users = profile.following.all()


        following_profiles = Profile.objects.filter(user__in=following_users)

        following_usernames = [p.user.username for p in following_profiles]

        return Response({"following": following_usernames})
