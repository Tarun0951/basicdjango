from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
     path('signup/', views.signup_view, name='signup'),
    path('forgot-password/', auth_views.PasswordResetView.as_view(template_name='accounts/forgot_password.html'), name='forgot_password'),
    path('reset-password-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('change-password/', views.change_password_view, name='change_password'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
     path('profile/', views.profile_view, name='profile'),
     path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout')

]

