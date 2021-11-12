from django.db import models


class Tendency(models.Model):
    LocationType = (  # 성별
        ('INDOOR', '실내'),
        ('OUTDOOR', '실외'),
    )
    LType = models.CharField(max_length=8, choices=LocationType)    # 실내/외 타입
