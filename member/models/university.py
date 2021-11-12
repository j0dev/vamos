from enum import Enum

from django.db import models


class CityType(Enum):
    SEOUL = '서울'
    BUSAN = '부산'
    DAEGU = '대구'
    INCHEON = '인천'
    GWANGJU = '광주'
    DAEJEON = '대전'
    ULSAN = '울산'
    GANGWON = '강원'
    CHUNGBUK = '충북'
    CHUNGNAM = '충남'
    JEONBUK = '전북'
    JEONNAM = '전남'
    GYEONGBUK = '경북'
    GYEONGNAM = '경남'
    JEJU = '제주'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class University(models.Model):
    name = models.CharField(max_length=64, null=True, unique=True)     # 학교 이름
    city = models.CharField(max_length=16, choices=CityType.choices())  # 학교 위치 (서울 부산 등, 상세위치 X)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "대학"
        verbose_name_plural = '대학'





