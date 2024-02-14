from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
from .api_views import UserRegisterAPIView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('register/', UserRegisterAPIView.as_view(), name='register')
    
]
