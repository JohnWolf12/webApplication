from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rejestracja/', views.register_view, name='rejestracja'),
    path('logowanie/', views.login_view, name='logowanie'),
    path('wylogowanie/', views.logout_view, name='wylogowanie'),

]
