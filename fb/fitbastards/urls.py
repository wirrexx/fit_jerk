from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_test, name='members'),
    path('<int:id>', views.profile_test, name='details'),
]