from demo.models import UserInfo
from rest_framework.views import APIView
from .serializer.sers import UserSerializer

# 会把序列化结果转成json格式
# 让客户端接收到的结果相比使用HttpResponse可读性更好
from rest_framework.response import Response


class UserInfoView(APIView):

    def get(self, request):
        # 获取所有结果
        user_info = UserInfo.objects.all()

        # 构建序列化器对象
        # many=True代表qs对象是一个列表，包含多个结果
        # 序列化时，使用的是instance参数
        serializer = UserSerializer(instance=user_info, many=True)

        """
        序列化器伪代码实现
        tmp = []

        for obj in user_info:
            d = {}
            d['name'] = obj.name
            d['Age'] = obj.age
            d['email'] = obj.email

            tmp.append(d)
            
        """
        return Response(serializer.data)

    def post(self, request):
        # 构建序列化器
        # 进行数据校验时，使用的是data参数
        serializer = UserSerializer(data=request.data)

        # 进行数据校验
        # 返回一个bool值，所有字段校验都通过返回True
        # 生成validated_data errors两个属性,挂载在serializer实例上
        if serializer.is_valid():
            # 校验成功
            new_list = UserInfo.objects.create(**serializer.validated_data)
            return Response(serializer.data)
        else:
            # 校验失败
            return Response(serializer.errors)