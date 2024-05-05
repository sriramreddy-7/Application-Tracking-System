from django.db import models
from django.utils import timezone
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