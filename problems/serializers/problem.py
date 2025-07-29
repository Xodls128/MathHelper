from rest_framework import serializers
from problems.models import Problem

class ProblemSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Problem
        fields = ['id', 'title', 'image', 'difficulty', 'created_at']
