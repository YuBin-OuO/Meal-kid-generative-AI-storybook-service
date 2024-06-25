from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
# app_name = 'account'
urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),  # 회원가입 URL
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]