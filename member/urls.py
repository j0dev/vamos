from rest_framework.routers import DefaultRouter
from django.urls import path, include

from member.views.memberView import MemberInfo

urlpatterns = [
    path("", MemberInfo.as_view())  # 사용자 정보 불러오기
]