from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'company', 'job_title', 'salary', 'notes', 'created_at', 'last_updated')
        model = Job
