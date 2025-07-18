from django.shortcuts import render
from rest_framework import authentication, permissions
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import user
from .serializers import UserSerializer

# Create your views here.

#@api_view
def api():
    pass


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_username(request):
    usernames=user.objects.all()
    serializer= UserSerializer(usernames,many=True)
    
    return Response({"Status":"Success","Welcome":request.user.username})
    