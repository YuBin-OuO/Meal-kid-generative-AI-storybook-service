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
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
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
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import login
from .forms import PasswordResetForm
def password_reset_request(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data['username'], email=form.cleaned_data['email'])
            subject = "비밀번호 재설정 요청"
            email_template_name = "accounts/password/password_reset_email.txt"
            c = {
                "email": user.email,
                'domain': request.get_host(),
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
                'protocol': 'http',
            }
            email = render_to_string(email_template_name, c)
            send_mail(subject, email, 'your_email@example.com', [user.email], fail_silently=False)
            return redirect("password_reset_done")
    else:
        form = PasswordResetForm()
    return render(request, "accounts/password/password_reset.html", {"form": form})

def password_reset_confirm(request, uidb64=None, token=None):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == "POST":
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return redirect('password_reset_complete')
        else:
            form = SetPasswordForm(user)
        return render(request, 'accounts/password/password_reset_confirm.html', {'form': form})
    else:
        return HttpResponse('비밀번호 재설정 링크가 유효하지 않습니다!')

def password_reset_done(request):
    return render(request, "accounts/password/password_reset_done.html")

def password_reset_complete(request):
    return render(request, 'accounts/password/password_reset_complete.html')