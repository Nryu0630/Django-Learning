from rest_framework import serializers
from ..models import UserInfo
<<<<<<< HEAD
=======

>>>>>>> 259d3de4da3836d4a60c4d03482e44e6194a545c

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
    
    def update(self, instance, validated_data):
        # 更新逻辑
        UserInfo.objects.filter(pk=instance.pk).update(**validated_data)
        updated_info = UserInfo.objects.get(pk=instance.pk)
        return updated_info
    
class UserSerializer2(serializers.ModelSerializer):
    # ModelSerializer类不仅会更具模型类生成序列化器，还会自动实现create和update方法
    # 缺点是模型类和序列化器类强耦合，灵活度降低

    # 定义返回的字段别名，会在fields的基础上加上自定义的字段
    Age = serializers.IntegerField(source="age")

    class Meta:
        model = UserInfo
        # 定义针对哪些字段进行序列化
        # fields = '__all__'
        # fields = ['name','age']
        exclude = ['age']
