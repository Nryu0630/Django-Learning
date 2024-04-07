from rest_framework import serializers
from ..models import UserInfo


# 序列化器的字段类型用于数据校验
class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=16)
    # 当需要返回的字段名和表中的字段名不同时
    # 可以使用source指定该字段对应表中的哪个字段
    Age = serializers.IntegerField(source="age")
    email = serializers.CharField(max_length=32)

    # 将create操作解耦到序列化器类中
    def create(self, validated_data):
        new_list = UserInfo.objects.create(**self.validated_data)
        return new_list
