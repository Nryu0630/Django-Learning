from rest_framework.generics import GenericAPIView
from .serializer.sers import UserSerializer, UserSerializer2
from demo.models import UserInfo
from rest_framework.response import Response
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
)


class UserInfoView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer2

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class UserInfoDetailView(
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView
):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer2

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.delete(request, pk)
