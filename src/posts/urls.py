from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from .views import PostView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', PostView.as_view(), name='posts'),
]
