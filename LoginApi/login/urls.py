from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import get_username

urlpatterns = [
    path("token/",TokenObtainPairView.as_view() ,name="Token"),
    path("get-username/",get_username,name="get-username"),
    path("token/refresh/",TokenRefreshView.as_view(),name="refresh-token")
]
