"""
URL mapping for the user API.
"""
from django.urls import path
from mail_auth import udemy_views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'user' # It's used for testing. I'm not implementing yet

urlpatterns = [
    path('udemy_register/', udemy_views.UdemyCreateUserView.as_view(), name='udemy_register'), 
    # name = udemy_register is used for tesgin. I'm not implementing yet
    path('udemy_token/',udemy_views.UdemyCreateTokenView.as_view(), name='udemy_token'),
    path('udemy_me/', udemy_views.UdemyManageUserView.as_view(), name='údemy_manage_me'),
    #JWT Authentication
    path("jwt/", TokenObtainPairView.as_view(), name="jwt_obtain_pair"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
]