from django.contrib.auth import views as auth_views
from . import views
from django.urls import  path

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.login, {'template_name': 'main/login.html'}, name='login'),
    path('logout/', auth_views.logout, name='logout'),
]
