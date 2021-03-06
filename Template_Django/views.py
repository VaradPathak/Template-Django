from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http.response import HttpResponseRedirect
# Create your views here.


def index(request):
    return render(request, 'index.html', {'name': 'Dude'})


def signup(request):
    email = request.POST['signup_email']
    password = request.POST['signup_password']
    first_name = request.POST['signup_first_name']
    last_name = request.POST['signup_last_name']
    username = email

    try:
        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return HttpResponseRedirect("/home", {'success': 'Successfully LoggedIn.'})
    except IntegrityError:
        return render(request, 'login.html', {'error': 'User already exists!! Try forgot password.'})


def signin(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/home", {'success': 'Successfully LoggedIn.'})

    if 'signIn_email' in request.POST:
        email = request.POST['signIn_email']
        password = request.POST['signIn_password']
        user = auth.authenticate(username=email, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect("/home", {'success': 'Successfully LoggedIn.'})
        else:
            # Show an error page
            return render(request, 'login.html', {'error': 'Invalid user try signup!!'})
    else:
        return render(request, 'login.html')


def home(request):
    if request.user.is_authenticated():
        return render(request, 'home.html', {'name': request.user.first_name})
    else:
        # Show an error page
        return HttpResponseRedirect("/signin", {'error': 'Invalid user please Signin!!'})


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return render(request, 'logout.html', {'success': 'You have been successfully logged out!!'})


def profile(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/home", {'success': 'Successfully LoggedIn.'})
    else:
        return render(request, 'login.html')
