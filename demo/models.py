from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=16)
    age = models.IntegerField(verbose_name="姓名")  # int
    email = models.CharField(verbose_name="邮箱", max_length=32)
