from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path("userInfo/", UserInfoView.as_view()),
]
