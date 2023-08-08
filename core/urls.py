from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cover'),
    path('home/', views.home, name='home'),
    path('signup/', views.SignUp, name='signup'),
    path('yield/', views.yieldinput, name='yield'),
    path('predict', views.predict, name='predict')
]
