from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'store/auth/register.html'
    success_url = reverse_lazy('login')

    """ При успешной регистрации вызывается данный метод и пользователь сразу же авторизуется и перенаправляется на home """
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')



class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'store/auth/login.html'

    ''' если пользователь успешно авторизовался, то вызывается данный метод, который перенаправляет на указанную страницу. '''
    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
