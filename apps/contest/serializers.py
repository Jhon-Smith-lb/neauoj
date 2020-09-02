from rest_framework import serializers
from .models import Contest
from apps.ojauth.serializers import UsersSerializer


class ContestListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contest
        fields = ('contest_id', 'title', 'private', 'user_id')


class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        exclude = ('defunct',)

