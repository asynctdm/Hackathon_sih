from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
 path('login/', views.Login, name='login'),
  path('', views.index, name='index'),
path('logout/', views.logout1, name='logout'),
] 