from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
        
        user.save()
        login(request, user)
        # return HttpResponse('User created successfully')
        return redirect('index') 
         
    return redirect('index') 

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('loginEmail')
        password = request.POST.get('loginPassword')
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            # return redirect('index')  #
            return redirect('index')
        else:
            return render(request, 'index.html', {'error': 'Invalid credentials'})
    return redirect('index') 


def logout_view(request):
    logout(request)
    return HttpResponse('User logged out successfully')