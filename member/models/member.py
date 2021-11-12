from enum import Enum
from django.contrib.auth.models import AbstractUser
from django.db import models
from member.util.memberManager import UserManager
from member.models.university import University


class Member(AbstractUser):
    GenderType = (  # 성별
        ('MALE', '남자'),
        ('FEMALE', '여자'),
    )
    objects = UserManager()
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)    # 사용자 이메일(ID)
    username = models.CharField(max_length=16, null=False, unique=False)     # 사용자 이름
    gender = models.CharField(max_length=8, choices=GenderType)   # 성별
    university = models.ForeignKey(University, null=True, on_delete=models.PROTECT)   # 소속 대학
    profile = models.ImageField(null=True, upload_to='profile', default='profile/default.png')  # 사용자 프로파일 이미지
    createdAt = models.DateTimeField(auto_now_add=True) # 계정 생성 시각
    activeAt = models.DateTimeField(auto_now_add=False, null=True)  # 이메일 인증(학교)
    is_agreement = models.BooleanField(default=False, null=True)   # 이용 약관 동의 여부
    is_active = models.BooleanField(default=False)  # 계정 인증 여부
    is_admin = models.BooleanField(default=False)   # 관리자 여부
    is_superuser = models.BooleanField(default=False)   # 최고 권한 관리자 여부
    USERNAME_FIELD = 'email'    # 이메일을 로그인 인증 아이디 사용
    REQUIRED_FIELDS = ['username']  # 기존 username 필드도 사용

    # 참여 모임
        # 모임 primary key
        # 상태 : 신청/
    # 내 모임
        # 모임 primary key
        #
    # 관심 모임
        # 모임 primary key
    # 관심 레저


    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "사용자"
        verbose_name_plural = '사용자'
