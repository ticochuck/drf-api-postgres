from django.urls import path

from .views import JobDetails, JobList

urlpatterns = [
    path('', JobList.as_view(), name='job_list'),
    path('<int:pk>/', JobDetails.as_view(), name='job_details'),
]
