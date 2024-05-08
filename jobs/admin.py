from django.contrib import admin

# Register your models here.
from jobs.models import JobApplication,EmailSubscription,UserJobApplication,RecommendedWebsite

admin.site.register(JobApplication)
admin.site.register(EmailSubscription)
admin.site.register(UserJobApplication)
admin.site.register(RecommendedWebsite)