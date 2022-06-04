"""
Views for the user API. Copied from Udemy Python/Django Advanced Course
"""
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from mail_auth.udemy_serializers import (
    UdemyUserSerializer,
    UdemyAuthTokenSerializer,
)

class UdemyCreateUserView(generics.CreateAPIView):
    """Create a new user in the syste. copied form Udemy"""
    serializer_class = UdemyUserSerializer
    permission_classes = [permissions.AllowAny]


class UdemyCreateTokenView(ObtainAuthToken):
    """Create a new auth token for user. copied from Udemy"""
    serializer_class = UdemyAuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UdemyManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user. """
    serializer_class = UdemyUserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [permissions.AllowAny]

    def get_object(self):
        return self.request.user