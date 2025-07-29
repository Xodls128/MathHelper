from rest_framework import serializers
from problems.models import ProblemTag

class ProblemTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemTag
        fields = ['id', 'name']
