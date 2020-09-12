from django.shortcuts import render
from rest_framework import generics

from .models import Job
from .permissions import IsAuthOrReadOnly
from .serializers import JobSerializer


class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthOrReadOnly,)
    queryset = Job.objects.all()
    serializer_class = JobSerializer
