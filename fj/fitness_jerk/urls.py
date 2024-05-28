from django.contrib.auth import views as auth_views
from django.urls import path
from .views import index_view

urlpatterns = [
    path("", index_view, name="index"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]