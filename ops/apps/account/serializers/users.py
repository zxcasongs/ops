from rest_framework import serializers
from apps.account.models import User


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = all
        depth = 1
