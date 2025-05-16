from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')  # Optional

urlpatterns = [
    path('', include(router.urls)),
    #path('posts/', PostView.as_view(), name='posts'),
]
