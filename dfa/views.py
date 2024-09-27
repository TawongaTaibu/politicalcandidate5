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
        HttpResponse: The rendered homepage template.
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
        HttpResponse: The rendered login template or redirect to the news page.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('news_list')  # Redirect to the news page after successful login
        else:
            messages.error(request, "Invalid username or password.")  # Display an error message for invalid login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def registration(request):
    """
    Handle user registration process.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered registration template or redirect to the login page.
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
    View a specific news item, requiring the user to be logged in.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The ID of the news item to view.

    Returns:
        HttpResponse: The rendered news view template.
    """
    selected_news = get_object_or_404(News, id=id)
    return render(request, 'News_View.html', {'selected_news': selected_news})

def news_list(request):
    """
    Display a list of all news items.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered news list template.
    """
    news_items = News.objects.all()
    return render(request, 'news_list.html', {'news_items': news_items})
