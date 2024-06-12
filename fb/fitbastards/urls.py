from django.urls import path
from . import views
from django import forms 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", LoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('signup/', views.signup_view, name="signup"),
    path('passwd-reset', views.password_reset_view, name="passwd_reset"),
    path('accounts/profile/', views.profile_view, name='details'), 
    path('settings/', views.settings_view, name='settings'),
    path('finish', views.workout_finish, name='finish'),
    path('<int:id>/delete', views.delete_view, name='delete'),
    path("exercise-loose/", views.weight_loose, name="exercise_loose"),
    path("exercise-tone/", views.tone_down, name="exercise_tone"),
    path("exercise-muscles/", views.build_muscles, name="exercise_muscles"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)