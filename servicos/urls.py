from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('addservico/', views.addServico, name="add-servico"),
    path('servico/<int:id>', views.servicoView, name='servico-view'),
  
] 