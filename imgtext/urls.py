from xml.etree.ElementInclude import include
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import PasswordsChangeView
urlpatterns = [
    path('', views.home, name="home"),
    path('openC', views.openC, name="openC"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('text1', views.text2, name="text1"),
    path('accounts/register/', views.register, name="register"),
    path('password', PasswordsChangeView.as_view(template_name='registration/changepassword.html'))
]
