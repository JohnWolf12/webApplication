from django.contrib.auth.views import LoginView
from django.urls import path

from . import views
from .forms import LoginForm

urlpatterns = [
    path('', views.index, name='index'),
    path('rejestracja/', views.register_view, name='rejestracja'),
    path('logowanie/', LoginView.as_view(template_name='aplikacjaogloszeniowa/login.html', authentication_form=LoginForm, next_page='/'), name='logowanie'),
    path('wylogowanie/', views.logout_view, name='wylogowanie'),

]
