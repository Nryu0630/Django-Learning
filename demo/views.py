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

        # serializer.data时才真正执行序列化操作
        return Response(serializer.data)

    def post(self, request):
        # 构建序列化器
        # 进行数据校验时，使用的是data参数
        serializer = UserSerializer(data=request.data)

        # 进行数据校验
        # 返回一个bool值，所有字段校验都通过返回True
        # 生成validated_data errors两个属性,挂载在serializer实例上
        # 校验时是按照序列化器的键名进行循环校验
        if serializer.is_valid():
            # 校验成功
            # new_list = UserInfo.objects.create(**serializer.validated_data)

            # 通过查看源码,序列化时实际上是在对self.instance进行序列化
            # 因此如果自定义的create方法没有return结果值,self.instancce就会为空
            # 导致serializer.data无法正常拿到结果
            serializer.save()

            return Response(serializer.data)
        else:
            # 校验失败
            return Response(serializer.errors)


# 对于对单条记录做操作的接口会多一个id参数
# 同时一个类中不可以有两个get方法
class UserInfoDetailView(APIView):

    def get(self, request, id):
        user_info = UserInfo.objects.get(pk=id)
        serializer = UserSerializer(isinstance=user_info, many=False)
        return Response(serializer.data)

    def put(self, request, id):
        # 获取提交的更新数据
        print("data:", request.data)
        update_info = UserInfo.objects.get(pk=id)

        # 构建序列化器对象
        serializer = UserSerializer(instance=update_info, data=request.data)

        if serializer.is_valid():
            # 更新逻辑
            UserInfo.objects.filter(pk=id).update(**serializer.validated_data)
            # 获取更新后的数据，返回给客户端
            updated_info = UserInfo.objects.filter(pk=id)
            serializer.instance = updated_info
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, id):
        UserInfo.objects.get(pk=id).delete()
        return Response()
