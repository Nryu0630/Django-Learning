from rest_framework.generics import GenericAPIView
from .serializer.sers import UserSerializer, UserSerializer2
from demo.models import UserInfo
from rest_framework.response import Response


class UserInfoView(GenericAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer2

    def get(self, request):
        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request):
        # 构建序列化器对象
        serializer = self.get_serializer(data=request.data)
        # 校验数据
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            # 校验失败
            return Response(serializer.errors)


class UserInfoDetailView(GenericAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserSerializer2

    def get(self, request, pk):
        # get_object方法会根据有名分组pk参数获取对象
        serializer = self.get_serializer(instance=self.get_object(), many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = self.get_serializer(
            instance=self.get_object(), data=request.data, many=False
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object().delete()
        return Response()
