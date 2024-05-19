"""
URL configuration for ATS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from jobs import views
from django.conf import settings
# from django.views.static import serve as static_serve
# from django.views.generic import RedirectView
# from django.urls import re_path
# from django.conf.urls.static import static

from jobs.views import AdsTxtView


urlpatterns = [
    path('ads.txt', views.AdsTxtView.as_view(), name='ads.txt'),
    
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('subscribe-newsletter/', views.subscribe_newsletter, name='subscribe_newsletter'),
    # path('navbar/', views.navbar, name='navbar'),
    # path("home/", views.home, name="home"),
    path("my_applications",views.my_applications,name="my_applications"),
    path("resume_tips",views.resume_tips,name="resume_tips"),
    path("test",views.test,name="test"),
    path('posts/', views.posts, name='posts'),
    path('add/', views.add_application, name='add_application'),
    path('edit/<int:application_id>/', views.edit_application, name='edit_application'),
    path('delete/<int:application_id>/', views.delete_application, name='delete_application'),
    
    
    #auth urls\
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path('accounts/login/', views.login_view, name='login'),
    
    #user urls
  
    path('job-application-tracker', views.job_application_tracker, name='job_application_tracker'),
    path('add-job-application', views.add_job_application, name='add_job_application'),
    path('edit-job-application/<int:user_job_application_id>/', views.edit_job_application, name='edit_job_application'),
    path('delete-job-application/<int:user_job_application_id>/', views.delete_job_application, name='delete_job_application'),
]
    
# urlpatterns += [
#     # re_path(r'^ads\.txt$', static_serve, {'path': 'ads.txt', 'document_root': settings.STATIC_ROOT}),
#     re_path(r'^ads\.txt$', views.ads_txt),
# ]

# if settings.DEBUG:
#     from django.conf.urls.static import static
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

