from basic_app import views
from django.urls import path
from django.contrib import admin


# TEMPLATE URLs
app_name = 'basic_app'


urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]
