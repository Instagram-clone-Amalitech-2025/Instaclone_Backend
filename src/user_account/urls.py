from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, LogoutView
from .views import UserDetailView
from .views import PasswordResetConfirmView
from . import views

urlpatterns = [
    # Custom authentication endpoints
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('password-reset/', views.PasswordResetRequestView.as_view(), name='request_password_reset'),
    path('confirm-password/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # Allauth URLs for login, registration, etc.
    path('accounts/', include('allauth.urls')),  # Handles allauth URLs for login, registration, etc.
    # Social authentication URLs (Google, Apple, etc.)
    path('auth/', include('social_django.urls', namespace='social')),  # Handles social login
]