from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserSessionData
from django.http import HttpResponse
def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'registration/profile.html')

def custom_logout(request):
    if request.user.is_authenticated:
        user_session, created = UserSessionData.objects.get_or_create(user=request.user)
        # 현재 세션 데이터를 저장
        user_session.session_data = dict(request.session)
        user_session.save()
    
    auth_logout(request)
    return redirect('login')

from django.http import HttpResponse
@login_required
def set_session_data(request):
    request.session['key'] = f"Value for user {request.user.username}"
    return HttpResponse(f"Session data set for user {request.user.username}")

@login_required
def get_session_data(request):
    value = request.session.get('key', 'No data found')
    return HttpResponse(f"Session data for user {request.user.username}: {value}")