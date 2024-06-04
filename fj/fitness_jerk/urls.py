from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import delete_user_func, logout_endpoint, password_reset_view, profile_view, profile_test, settings_view, signup_view, LoginView, workout_finish



urlpatterns = [
    #path("testview/", testview, name="testview"),
    path("", LoginView.as_view(), name="login"),
    path("profile/", profile_view, name="profile"),
    path('logout/', logout_endpoint, name='logout'),
    #path('complete_profile/', complete_profile, name="complete_profile"),
    path('signup/', signup_view, name="signup"),
    path('passwd-reset', password_reset_view, name="passwd_reset"),
    # path('', views.login_test, name='members'),
    path('<int:id>', profile_test, name='details'),
    path("logout/", logout_endpoint, name="logout"),
    path('<int:id>/settings', settings_view, name='settings'),
    path('<int:id>/finish', workout_finish, name='finish'),
    path('<int:id>/delete', delete_user_func, name='delete'),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

