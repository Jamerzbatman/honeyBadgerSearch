# accounts/views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login

from django.contrib.auth.forms import AuthenticationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            return redirect('sign_in')  # Redirect to the sign-in page after registration
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def custom_login(request):
    form = AuthenticationForm(data=request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
        return redirect('home')  # Redirect to home after login
