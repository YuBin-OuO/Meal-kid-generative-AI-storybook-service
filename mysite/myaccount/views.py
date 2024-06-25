from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserSessionData
from django.http import HttpResponse

# def base(request):
#     return render(request, 'base.html')

def index(request):
    return render(request, 'index.html')

from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            request.session['user_email'] = user.email
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'registration/profile.html')

def custom_logout(request):
    if request.user.is_authenticated:
        user_session, created = UserSessionData.objects.get_or_create(user=request.user)
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

from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.conf import settings

def password_reset_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            temp_password = get_random_string(8)
            user.set_password(temp_password)
            user.save()

            send_mail(
                '임시 비밀번호',
                f'임시 비밀번호는 {temp_password}입니다. 로그인 후 비밀번호를 재설정하세요.',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            return redirect('password_reset_done')
    return render(request, 'registration/password_reset.html')