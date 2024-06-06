from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import delete_user_func, logout_endpoint, profile_view, profile_test, settings_view, signup_view, LoginView, workout_finish, CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView, CustomPasswordChangeDoneView, CustomPasswordChangeView

# proof of concept passwd reset
from django.contrib.auth import views as auth_views


urlpatterns = [
    ## Auth
    # Password management
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password-change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),

    # Signin/Signout/Signup
    path('logout/', logout_endpoint, name='logout'),
    path("", LoginView.as_view(), name="login"),
    path('signup/', signup_view, name="signup"),
    
    path("profile/", profile_view, name="profile"),
    path('<int:id>', profile_test, name='details'),
    path('<int:id>/settings', settings_view, name='settings'),
    path('<int:id>/finish', workout_finish, name='finish'),
    path('<int:id>/delete', delete_user_func, name='delete'),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

