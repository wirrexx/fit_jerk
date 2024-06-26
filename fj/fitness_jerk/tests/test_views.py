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
        #+ id is set is set so because otherwise Uniq constraint might be triggered in Members.objects.create(user=user)
        response = self.client.post(reverse("signup"), {"username":"testuser", "email":"testuser@example.com", "password1":"test238(89&%$)", "password2":"test238(89&%$)", "id":"3000000000000"}) # id 
        
        # check that response redirects
        self.assertEqual(response.status_code, 302)
        
        # check that response redirects to the correct url
        self.assertRedirects(response, reverse("profile"))

        
    def test_signup_view_POST_with_invalid_user(self):
        response = self.client.post(reverse("signup"), {"username":"testuser", "email":"testuser@example.com", "password1":"test238(89&%$)", "password2":"t&%$)"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")


class TestPasswordRelatedViews(TestCase):
    # setup 
    def setUp(self):
        testuser = User.objects.create_user(username="testuser", email="testuser@example.com", password="Wr3{j:J%$2]UH<su-~fdyD~Ky)&&yb&M'.hq\rV%")

    # CustomPasswordResetView
    def test_CustomPasswordResetView_url_exists_at_right_location(self):
        response = self.client.get("/password-reset/")
        self.assertEqual(response.status_code, 200)

    def test_CustomPasswordResetView_url_accessible_by_name(self):
        response = self.client.get(reverse("password_reset"))
        self.assertEqual(response.status_code, 200)

    def test_CustomPasswordResetView_uses_correct_template(self):
        response = self.client.get(reverse("password_reset"))
        self.assertTemplateUsed(response, "registration/custom_password_reset_form.html") 

    def test_CustomPasswordResetView_succes_url(self):
        response = self.client.post(reverse("password_reset"), {"email":"testuser@example.com"})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("password_reset_done"))


    def test_CustomPasswordResetView_confirm(self):
        # mock link
        # access link
        # give two new passwords
        # assertEquel: user.password password given