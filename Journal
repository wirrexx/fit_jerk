## Implementing Password Reset

- settings.py

For development purposes, the console backend is useful as it prints the email to the console. For production, replace it with appropriate SMTP settings.

- urls.py

urlpatterns = [
path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]

- templates/registration/

password_reset_form.html
password_reset_done.html
password_reset_confirm.html
password_reset_complete.html

- Optional: Email Templates
password_reset_subject.txt
password_reset_email.html

