from django.urls import path, re_path, include

# from .views import *
# from .generateApiView import *
# from .mixinView import *
from .viewSetview import *

urlpatterns = [
    # path("userInfo/", UserInfoView.as_view()),
    # re_path("userInfo/(\d+)", UserInfoDetailView.as_view()),
    # path("userInfo/", UserInfoView.as_view()),
    # re_path("userInfo/(?P<pk>\d+)", UserInfoDetailView.as_view()),
    path("userInfo/", UserInfoView.as_view({"get": "get_all", "post": "add_object"})),
    re_path(
        "userInfo/(?P<pk>\d+)",
        UserInfoView.as_view(
            {"get": "get_object", "put": "update_object", "delete": "delete_object"}
        ),
    ),
]
