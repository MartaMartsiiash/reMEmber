"""
Views related to user authentication and profile management.
"""


from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.decorators import login_required


def root_redirect(request):
    """
    Redirects the root URL to the login page.
    """
    return redirect('log_in')

def signup(request):
    """
    Handle user registration.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('notes')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

def log_in(request):
    """
    Handle user login.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('notes')
        else:
            form.add_error(None, "Неправильні дані для входу")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def profile(request):
    """
    Handle user profile editing.
    """
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'users/profile.html', {'form': form})

@login_required
def log_out(request):
    """
    Log out the current user and redirect to the login page.
    """
    logout(request)
    return redirect('log_in')
