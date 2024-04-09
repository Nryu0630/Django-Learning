from rest_framework.response import Response
from demo.models import UserInfo
from .serializer.sers import UserSerializer, UserSerializer2
from rest_framework.viewsets import ModelViewSet


class UserInfoView(ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer
