from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login_test, name='members'),
    path('<int:id>', views.profile_test, name='details'),
    path("logout/", views.member_logout, name="logout"),
    path('<int:id>/settings', views.settings, name='settings'),
    path('<int:id>/finish', views.workout_finish, name='finish'),
    path('<int:id>/delete', views.delete, name='delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)