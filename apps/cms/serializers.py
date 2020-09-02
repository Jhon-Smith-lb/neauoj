from rest_framework import serializers
from apps.ojauth.models import Users


class CmsUsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = ('volume', 'language')


