from rest_framework import serializers
from member.models import University


class UniversitySerializer(serializers.ModelSerializer):
    # University Model Serializer
    class Meta:
        model = University
        fields = (
            'pk',
            'name',
        )
        read_only_fields = ('pk', 'name')