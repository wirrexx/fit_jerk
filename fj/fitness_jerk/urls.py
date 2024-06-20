from allauth.socialaccount.providers.google.views import oauth2_login as google_login
from allauth.socialaccount.providers.google.views import oauth2_callback as google_callback
from allauth.socialaccount.views import signup as socialaccount_signup

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import delete_user_func, logout_endpoint, profile_view, settings_view, signup_view, LoginView, workout_finish, CustomPasswordResetView, CustomLoginView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView, CustomPasswordChangeDoneView, CustomPasswordChangeView, LandingPage, AboutPage, PrivacyPolicyView, ImprintView
from . import views


urlpatterns = [    
    ## Auth
    # Password management
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),

    # Signin/Signout/Signup/Landing
    path('logout/', logout_endpoint, name='logout'),
    path("login/", CustomLoginView.as_view(), name="login"),
    path('signup/', signup_view, name="signup"),

    # OAuth 
    path('accounts/google/login/', google_login, name='google_login'),
    path('accounts/google/login/callback/', google_callback, name='google_callback'),    
    path('accounts/social/signup/', socialaccount_signup, name='socialaccount_signup'),  
    
    #Training Functions
    path("exercise-loose/", views.weight_loose, name="exercise_loose"),
    path("exercise-tone/", views.tone_down, name="exercise_tone"),
    path("exercise-muscles/", views.build_muscles, name="exercise_muscles"),


    #Main pages
    path('', LandingPage.as_view(), name="welcome"),
    path('about/', AboutPage.as_view(), name="about"),
    path("profile/", profile_view, name="profile"),
    path('settings/', settings_view, name='settings'),
    path('finish', workout_finish, name='finish'),
    path('delete', delete_user_func, name='delete'),
    path("imprint.html", ImprintView.as_view(), name="imprint"),
    path("privacy-policy.html", PrivacyPolicyView.as_view(), name="privacy_policy"),
    
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)