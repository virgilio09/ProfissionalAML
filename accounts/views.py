from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import userForm

class UserCreationForm(generic.CreateView):
    form_class = userForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'