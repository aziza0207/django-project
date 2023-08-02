from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.response.user
