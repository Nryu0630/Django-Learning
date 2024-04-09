from .serializer.sers import UserSerializer, UserSerializer2
from demo.models import UserInfo
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


class UserInfoView(ViewSet):

    def get_all(self, request):
        return Response("查看所有资源")

    def add_object(self, request):
        return Response("添加资源")

    def get_object(self, request, pk):
        return Response("查看单一资源")

    def update_object(self, request, pk):
        return Response("更新单一资源")

    def delete_object(self, request, pk):
        return Response("删除单一资源")
