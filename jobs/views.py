from django.shortcuts import render, redirect
from jobs.models import JobApplication, EmailSubscription
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site

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

        # Send email to subscribed users
        send_newsletter_to_subscribers()

        return redirect('index')
    else:
        applications = JobApplication.objects.all()
        # send_newsletter_to_subscribers()
        return render(request, 'index.html', {'applications': applications})




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