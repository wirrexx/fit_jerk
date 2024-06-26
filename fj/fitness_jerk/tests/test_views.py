from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from fitness_jerk.views import signup_view
from fitness_jerk.forms import FitUserForm


class TestSignupView(TestCase):
    
    def test_signup_view_GET(self):
        response = self.client.get(reverse("signup"))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")
        self.assertIsInstance(response.context["form"], FitUserForm)
    

    def test_signup_view_POST_with_valid_user(self):
        # simulate post request with valid form data
        response = self.client.post(reverse("signup"), {"username":"testuser", "email":"testuser@example.com", "password1":"test238(89&%$)", "password2":"test238(89&%$)", "id":"3000000000000"}) # id is set so high because otherwise Uniq constraint might be triggered in Members.objects.create(user=user)
        
        # check that response redirects
        self.assertEqual(response.status_code, 302)
        
        # check that response redirects to the correct url
        self.assertRedirects(response, reverse("profile"))

        
    def test_signup_view_POST_with_invalid_user(self):
        response = self.client.post(reverse("signup"), {"username":"testuser", "email":"testuser@example.com", "password1":"test238(89&%$)", "password2":"t&%$)"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")


