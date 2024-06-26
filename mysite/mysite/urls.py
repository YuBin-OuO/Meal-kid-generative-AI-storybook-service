"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from myaccount import views as account_views
def base(request):
    return render(request,'base.html')

def index(request):
    return render(request,'index.html')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index),
    path('base/', base),
    path('myaccount/', include('django.contrib.auth.urls')),  
    path('myaccount/', include('myaccount.urls')),
    path('myaccount/', include('allauth.urls')),  
    path('signup/', account_views.signup, name='signup'),  # 회원가입 URL
    #path('myaccounts/profile/', account_views.profile, name='profile'),
    path('', account_views.index, name='index'),
    path('reader/', include('reader.urls')),
    path('generator/', include('generator.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
