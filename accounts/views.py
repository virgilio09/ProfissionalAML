from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from .forms import userForm, editProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView

class UserCreationForm(generic.CreateView):
    form_class = userForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
   

class UserEditView(generic.UpdateView):
    form_class = editProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('edit_success')
   
    def get_object(self):
        return self.request.user

def editSuccess(request):
    messages.success(request, "Informaçãos alteradas com sucesso!")
    return redirect('dashboard')

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('password_success')

def passwordSuccess(request):
    messages.success(request, "Senha alterada com sucesso!!")
    return redirect('dashboard')

def myAccount(request):
    return render(request, 'my_account.html')