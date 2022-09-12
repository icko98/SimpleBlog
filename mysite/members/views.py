from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.



def login_user(request):


    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        # Redirect to a success page.
            return redirect('/')
        else:
        # Return an 'invalid login' error message.
            messages.success(request, ("Error logging in, try again."))
            return redirect('/members/login_user')
    else:
        return render(request, 'authenticate/login.html', {})
    
def logout_user(request):


    logout(request)
    messages.success(request, ("You are now logged out."))
    return redirect('/')

def register_user(request):


    if request.method=="POST":
        print("RADI")
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        messages.success(request, ("Register sucessful."))
        return redirect('/members/login_user')
    else:
        return render(request, 'authenticate/register.html', {})
