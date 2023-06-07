from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('history/', views.history, name='history'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

