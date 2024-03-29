from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from accounts.models import User
from accounts.serializers import UserRegisterSerializers


class UserRegisterAPIView(GenericAPIView):
    """" Api for registering user"""
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


###### HERE WE CAN ALSO SPECIFY LOGIN API AND GIVE TOKEN MANUALLY BUT I'M DIRECTLY USING JWT ######