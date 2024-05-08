from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class JobApplication(models.Model):
    s_no = models.AutoField(primary_key=True)
    company = models.CharField(max_length=100,blank=True)
    role = models.CharField(max_length=100,blank=True)
    deadline = models.DateTimeField(blank=True)
    status = models.CharField(max_length=50,blank=True)
    link = models.URLField(max_length=200,blank=True)
    remarks = models.TextField(blank=True)
    medium = models.CharField(max_length=50,blank=True)
    posted_on = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.company
    
    
class EmailSubscription(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    
class UserJobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE)
    application_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)
    posted_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s Application for {self.job_application.company}"



class RecommendedWebsite(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.name
