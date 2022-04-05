from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('openC', views.openC, name="openC"),
    path('text1', views.text2, name="text1"),
    path('accounts/register/', views.register, name="register")
]
