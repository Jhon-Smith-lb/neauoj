from rest_framework import serializers
from .models import Problem


class ProblemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('problem_id', 'title', 'source', 'accepted', 'submit')


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        exclude = ('spj', 'in_date', 'defunct')

