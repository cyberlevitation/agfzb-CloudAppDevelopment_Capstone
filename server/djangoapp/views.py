from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def get_dealerships(request):
    return render(request, 'djangoapp/index.html')

# Create an `about` view to render a static about page
# def about(request):
# ...
def about(request):
    return render(request, 'djangoapp/about.html')


# Create a `contact` view to return a static contact page
#def contact(request):
def contact(request):
    return render(request, 'djangoapp/contact.html')

# Create a `login_request` view to handle sign in request
# def login_request(request):
# ...
def login_request(request):
    context = {}
    # Handles POST request
    if request.method == "POST":
        # Get username and password from POST request
        username = request.POST['username']
        password = request.POST['psw']
        # Check for authentication of provided credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # Call login method to login current user if user is valid
            login(request, user)
            return redirect('djangoapp:index')
        else:
            # if not, return to home page 
            return render(request,'djangoapp/index.html', context)
    else:
        return render(request,'djangoapp/index.html', context)

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...
def logout_request(request):
    # Get the user object based on session id in request
    print("Log out the user `{}`".format(request.user.username))
    # Logout user in the request
    logout(request)
    # Redirect user back to course list view
    return redirect('djangoapp:get_dealerships')

# Create a `registration_request` view to handle sign up request
# def registration_request(request):
# ...
def registration_request(request):
    context = {}
    # if it is a GET request, render the registration page 
    if request.method == 'GET'
        return render(request, 'djangoapp/registration.html', context)
    # If POST request 
    elif request.method == 'POST':
        # Get user information from POST request 
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            # Check if user already exists 
            User.objects.get(username=username)
            user_exist = True
        except:
            # If not, log this user as a new user 
            logger.debug("{} is new user".format(username))
        # If a new user 
        if not user_exist:
            # Add user to auth_user table 
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password)
            # Login user and redirect to review list page 
            login(request, user)
            return redirect("djangoapp:index")
        else:
            return render(request, 'djangoapp/registration.html', context)

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

