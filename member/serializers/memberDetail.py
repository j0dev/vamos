from collections import OrderedDict

import six
from rest_framework import serializers
from rest_framework.fields import ChoiceField

from member.models import Member
from member.serializers.universityDetail import UniversitySerializer


class ChoiceDisplayField(ChoiceField):      # choice(enum) 객체 key, value 반환
    def __init__(self, *args, **kwargs):
        super(ChoiceDisplayField, self).__init__(*args, **kwargs)
        self.choice_strings_to_display = {
            six.text_type(key): value for key, value in self.choices.items()
        }
        print(self.choice_strings_to_display)

    def to_representation(self, value):
        if value in ('', None):
            return value
        if '.' in value:
            value = value.split('.')[1]
        return {
            'key': self.choice_strings_to_values.get(six.text_type(value), value),
            'value': self.choice_strings_to_display.get(six.text_type(value), value),
        }


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    university = UniversitySerializer(read_only=True)
    gender = ChoiceDisplayField(choices=Member.GenderType)

    class Meta:
        model = Member
        fields = (
            'pk',
            'email',
            'username',
            'gender',
            'university',
            'profile',
        )
        read_only_fields = ('pk', 'email', 'username', 'gender', 'university', 'profile')


