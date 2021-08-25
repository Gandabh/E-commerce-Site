from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from account.models import User
from account.api.serializers import UserDetailSerializer
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListCreateAPIView

from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from account.tasks import send_confirmation_mail
from django.contrib import messages




class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user_serializer = UserDetailSerializer(user)
        return Response(user_serializer.data, status=200)



# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        send_confirmation_mail(user)
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

