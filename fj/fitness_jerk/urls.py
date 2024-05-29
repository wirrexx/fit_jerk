from django.urls import path
from .views import complete_profile, password_reset_view, profile_view,  signup_view, LogoutView, LoginView, test_form_view, test_endpoint
urlpatterns = [
    # Testform paths
    path("testform", test_form_view, name="testform"),
    path("thanks/", test_endpoint, name="testendpoint"),
    
    path("", LoginView.as_view(), name="login"),
    path("profile/", profile_view, name="profile"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('complete_profile/', complete_profile, name="complete_profile"),
    path('signup/', signup_view, name="signup"),
    path('passwd-reset', password_reset_view, name="passwd_reset")
]