from django.contrib.auth.models import User
from django.db import models


class Job(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=64)
    job_title = models.CharField(max_length=64)
    salary = models.IntegerField()
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.job_title}, {self.company}'
    