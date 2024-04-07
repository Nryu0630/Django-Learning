from django.urls import path, re_path, include

# from .views import *
# from .generateApiView import *
from .mixinView import *

urlpatterns = [
    # path("userInfo/", UserInfoView.as_view()),
    # re_path("userInfo/(\d+)", UserInfoDetailView.as_view()),
    path("userInfo/", UserInfoView.as_view()),
    re_path("userInfo/(?P<pk>\d+)", UserInfoDetailView.as_view()),
]
