from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as authview
from .views import *
from .authentications import *


app_name = 'home'

urlpatterns = [
    path('', home, name = 'home'),
    path('signup/', signup, name = 'signup'),
    # path('login/', user_login, name = 'login'),
    path('dashboard/', profile, name = 'profile'),
    path('login/', logout_required(authview.LoginView.as_view(template_name='login.html')), name='login'),
	path('logout/', authview.LogoutView.as_view(), name='logout'),
]