# navigator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('login/', views.loginView, name='login'),           # Login page
    path('logout/', views.logoutView, name='logout'),  # Logout

    # User registration
    path('register/', views.register, name='register'),

    # Main app pages
    path('map/', views.map_view, name='map'),

    # API endpoint
    path('find-path/', views.find_path, name='find_path'),
]