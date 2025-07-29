from django.db import models

class ProblemTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Problem(models.Model):
    title = models.CharField(max_length=200)
    content = models.ImageField(upload_to='problem_images/')
    difficulty = models.IntegerField()
    tags = models.ManyToManyField(ProblemTag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
