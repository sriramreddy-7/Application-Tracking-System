from django.contrib import admin

# Register your models here.
from jobs.models import JobApplication,EmailSubscription,UserJobApplication

admin.site.register(JobApplication)
admin.site.register(EmailSubscription)
admin.site.register(UserJobApplication)