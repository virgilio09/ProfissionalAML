from django.contrib import auth
from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.UserCreationForm.as_view(), name='register'),
    path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
    path('password/', views.PasswordChangeView.as_view(), name='change_password'),
]