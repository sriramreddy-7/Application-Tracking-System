from django.shortcuts import render, redirect
from jobs.models import JobApplication, EmailSubscription
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

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
        return render(request, 'index.html', {'applications': applications})


def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        EmailSubscription.objects.create(email=email)
        send_confirmation_email(email)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
    
    
def send_newsletter_to_subscribers():
    print("Sending newsletter to subscribers")
    subject = 'New Job Application Added!'
    message = 'A new job application has been added. Check it out!'
    from_email = settings.EMAIL_HOST_USER
    email_subscriptions_count = EmailSubscription.objects.count()
    for i in range(email_subscriptions_count):
        recipient_list = [EmailSubscription.objects.all()[i].email]
        print(send_mail(subject, message, from_email, recipient_list, fail_silently=True))
    return redirect('index')


def send_confirmation_email(email):
    subject = 'Subscription Confirmation'
    message = 'Thank you for subscribing to our newsletter!'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=True)