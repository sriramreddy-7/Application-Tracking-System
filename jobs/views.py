from django.shortcuts import render, redirect
from jobs.models import JobApplication, EmailSubscription, UserJobApplication
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def test(request):
    job_applications = JobApplication.objects.all()
    return render(request, 'index.html', {'job_applications': job_applications})

def index(request):
    if request.method == 'POST':
        company = request.POST.get('company')
        role = request.POST.get('role')
        deadline = request.POST.get('deadline')
        status = request.POST.get('status')
        link = request.POST.get('link')
        remarks = request.POST.get('remarks')
        medium = request.POST.get('medium')

        JobApplication.objects.create(
            company=company,
            role=role,
            deadline=deadline,
            status=status,
            link=link,
            remarks=remarks,
            medium=medium
        )
        send_newsletter_to_subscribers()

        return redirect('index')
    else:
        job_applications = JobApplication.objects.all()
        return render(request, 'index.html', {'job_applications': job_applications})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('index') 
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'auth/login.html')

    return render(request, 'auth/login.html')

def signup(request):
    if request.method == 'POST':
        # username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return render(request, 'auth/signup.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Username is already taken")
            return render(request, 'auth/signup.html')
        
        user = User.objects.create_user(username=email, email=email, password=password1)
        login(request, user)
        
        messages.success(request, "You have successfully signed up!")
        return redirect('index') 

    return render(request, 'auth/signup.html')

def logout_view(request):
    logout(request)
    # Redirect to a specific URL after logout
    response = redirect('index')  # Replace 'home' with the URL name of your home page
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'  # HTTP 1.1
    response['Pragma'] = 'no-cache'  # HTTP 1.0
    response['Expires'] = '0'  # Proxies
    return response
    # return redirect('index')


@login_required
def my_applications(request):
    applications = JobApplication.objects.all()
    return render(request,'my_applications.html',{'applications': applications})


@login_required
def resume_tips(request):
    return render(request,'resume_tips.html')



def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if EmailSubscription.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
        else:
            EmailSubscription.objects.create(email=email)
            send_confirmation_email(email)
            messages.success(request, 'Email added to subscriber list')
    else:
        messages.error(request, 'Unable to add')
    return redirect('index')

from django.template.loader import render_to_string

def send_newsletter_to_subscribers():
    print("Sending newsletter to subscribers")
    subject = 'ATS Alerts: New Job Application Added!'
    from_email = settings.EMAIL_HOST_USER
    applications = JobApplication.objects.all()

    # Prepare the HTML content for the email
    html_content = render_to_string('email_template.html', {'applications': applications})

    # Get the list of subscribers' emails
    subscribers_emails = EmailSubscription.objects.values_list('email', flat=True)

    # Send email to each subscriber
    for email in subscribers_emails:
        send_mail(subject, '', from_email, [email], html_message=html_content, fail_silently=True)

    return redirect('index')



def send_confirmation_email(email):
    subject = 'Subscription Confirmation'
    message = 'Thank you for subscribing to our newsletter! Visit our site here: https://application-tracking-system-zf8k.onrender.com/'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=True)
    
    
    
def job_application_tracker(request):
    user_job_applications = UserJobApplication.objects.filter(user=request.user)
    jobs = JobApplication.objects.all()
    return render(request, 'job_application_tracker.html', {'user_job_applications': user_job_applications, 'jobs': jobs})

def add_job_application(request):
    if request.method == 'POST':
        user = request.user
        job_id = request.POST.get('job')
        job_application = JobApplication.objects.get(pk=job_id)
        application_date = request.POST.get('application_date')
        status = request.POST.get('status')
        notes = request.POST.get('notes')

        UserJobApplication.objects.create(user=user, job_application=job_application, application_date=application_date, status=status, notes=notes)
        return redirect('job_application_tracker')
    else:
        jobs = JobApplication.objects.all()
        return render(request, 'job_application_tracker.html', {'jobs': jobs})

def edit_job_application(request, user_job_application_id):
    user_job_application = UserJobApplication.objects.get(id=user_job_application_id)
    if request.method == 'POST':
        user_job_application.status = request.POST.get('status')
        user_job_application.notes = request.POST.get('notes')
        user_job_application.save()
        return redirect('job_application_tracker')
    else:
        return render(request, 'edit_job_application.html', {'user_job_application': user_job_application})

def delete_job_application(request, user_job_application_id):
    user_job_application = UserJobApplication.objects.get(id=user_job_application_id)
    user_job_application.delete()
    return redirect('job_application_tracker')