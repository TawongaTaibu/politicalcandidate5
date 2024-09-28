"""
views.py
--------

This module contains the views for handling the display and interaction
with the political party's web application.

Functions:
    home: Render the homepage with global warming data.
    login: Handle the user's login process.
    registration: Handle user registration process.
    News_View: View a specific news item (login required).
    news_list: Display a list of all news items.
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import CreateUserForm
from .models import News
from datetime import datetime

def home(request):
    """
    Render the homepage with global warming data.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered homepage template with global warming data
        as context variables.
    """
    global_warming_data = {
        'temperature_rise': '1.1°C',
        'sea_level_rise': '20cm',
        'co2_levels': '419 ppm'
    }
    return render(request, 'home.html', {'global_warming_data': global_warming_data})

def login(request):
    """
    Handle the user's login process.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the login form on GET request. On POST, attempts
        to log the user in and redirects to the news list page on success, or 
        re-renders the login template with an error message on failure.
    
    Raises:
        ValueError: If the provided credentials are invalid.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('news_list')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def registration(request):
    """
    Handle the user registration process.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Renders the registration form on GET request. On POST,
        it processes the user registration, saves the new user, and redirects
        to the login page on success.
    
    Raises:
        ValidationError: If the form data is invalid during the registration.
    """
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dfa:login')
    else:
        form = CreateUserForm()
    return render(request, 'registration.html', {'form': form})

@login_required
def News_View(request, id):
    """
    View a specific news item. This view requires the user to be logged in.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the news item to view.

    Returns:
        HttpResponse: The rendered news detail template displaying the selected
        news item.
    
    Raises:
        Http404: If no news item is found with the given ID.
    """
    selected_news = get_object_or_404(News, id=id)
    return render(request, 'News_View.html', {'selected_news': selected_news})

def news_list(request):
    """
    Display a list of all news items.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered news list template displaying all news items.
    """
    news_items = News.objects.all()
    return render(request, 'news_list.html', {'news_items': news_items})
