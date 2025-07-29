from django.db import models
from django.conf import settings
from problems.models import Problem

class Solutions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    
    #사용자 입력
    content = models.ImageField(upload_to='solution_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    #AI 처리 결과 (MCP 구현 후 적용예정)
    # ocr_text = models.TextField(null=True, blank=True)
    # logic_steps = models.JSONField(null=True, blank=True)
    # feedback_text = models.TextField(null=True, blank=True)
    # mistake_spot = models.JSONField(null=True, blank=True)
    # score = models.IntegerField(null=True, blank=True)
