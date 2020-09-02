from rest_framework import serializers
from .models import Solution


class SolutionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = '__all__'


