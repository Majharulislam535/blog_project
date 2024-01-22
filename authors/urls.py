from django.urls import path
from .import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('profile/',views.profile,name='profile'),
    path('pass_change/',views.pass_change,name='pass_change'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('LogOut/',views.LogOut,name='LogOut'),
]
