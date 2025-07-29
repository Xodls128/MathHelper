from rest_framework import serializers
from solutions.models import Solution

class SolutionSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)

    class Meta:
        model = Solution
        fields = [
            'id',
            'user',
            'problem',
            'image',
            'created_at',
            'ocr_text',
            'logic_steps',
            'feedback_text',
            'mistake_spot',
            'score',
        ]
        read_only_fields = ['user', 'ocr_text', 'logic_steps', 'feedback_text', 'mistake_spot', 'score']
