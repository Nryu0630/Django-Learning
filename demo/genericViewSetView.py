from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from demo.models import UserInfo
from .serializer.sers import UserSerializer, UserSerializer2
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
)
from rest_framework.generics import (
    # 单独封装
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    ListAPIView,
    RetrieveAPIView,
    # 对多条数据操作的混合封装
    ListCreateAPIView,
    # 对单条数据操作的混合封装
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView,
)


# 可以使用混合类
class UserInfoView(GenericViewSet, ListModelMixin):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer
