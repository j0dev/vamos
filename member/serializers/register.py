from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from member.models import University, Member
from allauth.account.adapter import get_adapter


class UniversityForeignKey(serializers.PrimaryKeyRelatedField):     # 대학 리스트
    def get_queryset(self):
        return University.objects.all()


class CustomRegisterSerializer(RegisterSerializer):
    # df rest auth 회원가입 로직 변경
    username = serializers.CharField(max_length=16)     # 사용자 이름
    gender = serializers.ChoiceField(choices=Member.GenderType)    # 성별
    university = UniversityForeignKey()     # 소속 대학
    profile = serializers.ImageField(allow_null=True, allow_empty_file=True)    # 프로필 이미지, 업로드 안해도 가입 가능

    def validate_username(self, username):
        # username = get_adapter().clean_username(username)
        # print(username)
        return username

    # transaction
    @transaction.atomic
    def save(self, request):
        university = University.objects.get(pk=self.data.get('university'))     # 선택한 대학 객체 생성
        user = super().save(request)    # 사용자 객체 생성
        user.gender = self.data.get('gender')
        user.university = university
        user.is_active = True
        user.save()
        return user     # 사용자 객체 반환