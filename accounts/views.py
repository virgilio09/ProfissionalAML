from django.urls import reverse_lazy
from django.views import generic
from .forms import userForm, editProfileForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

class UserCreationForm(generic.CreateView):
    form_class = userForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
   

class UserEditView(generic.UpdateView):
    form_class = editProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('dashboard')
   
    def get_object(self):
        return self.request.user

class PasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/password_change.html'
    success_url = reverse_lazy('dashboard')


 