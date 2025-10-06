from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, View

from accounts.forms import EmailUserCreationForm
from accounts.models import User


class HomePageView(TemplateView):
    def get(self, request, *args, **kwargs):

        return render(request, 'accounts/home-page.html')



class RegisterView(CreateView):
    form_class = EmailUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy("accounts:index")

    def form_valid(self, form):
        response = super().form_valid(form)

        username = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')

        user = authenticate(
            self.request,
            username=username,
            password=password
        )
        login(request=self.request, user=user)

        return response

class UpdatePersonalPage(UpdateView):
    template_name = "accounts/update_profile.html"
    model = User
    fields = "first_name", "last_name", "bio", "avatar"
    success_url = reverse_lazy("accounts:profile")

    def get_object(self, queryset=None):
        return self.request.user