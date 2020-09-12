from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Job


class JobTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username='testuser1', 
            password='testing12346'
        )
        
        testuser1.save()

        testjob = Job.objects.create(
            author=testuser1,
            company='Starbucks',
            job_title='Software Developer',
            salary=120000,
            notes='great coffee'
        )

        testjob.save()

    
    def test_blog_content(self):
        job = Job.objects.get(id=1)
        actual_author = str(job.author)
        actual_company = str(job.company)
        actual_job_title = str(job.job_title)
        actual_salary = job.salary
        actual_notes = str(job.notes)
        self.assertEqual(actual_author, 'testuser1')
        self.assertEqual(actual_company, 'Starbucks')
        self.assertEqual(actual_job_title, 'Software Developer')
        self.assertEqual(actual_salary, 120000)
        self.assertEqual(actual_notes, 'great coffee')

        
        
