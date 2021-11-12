from django.db import transaction
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from member.models import Member
from member.serializers.memberDetail import CustomUserDetailsSerializer


class MemberInfo(APIView):
    # tranaction
    @transaction.atomic
    def get(self, request):
        serializer = CustomUserDetailsSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)







