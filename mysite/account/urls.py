from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),  # 회원가입 URL
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('set-session/', views.set_session_data, name='set_session_data'),  # 세션 데이터 설정 URL
    path('get-session/', views.get_session_data, name='get_session_data'),  # 세션 데이터 가져오기 URL    
]
