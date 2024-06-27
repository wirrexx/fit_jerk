from django.contrib.auth.models import User
from django.test import TestCase 
from django.urls import reverse
from fitness_jerk.forms import FitUserForm, ProfileChangeForm, PictureChangeForm
from fitness_jerk.models import UserProfile

# -------------------------- XTN ---------------------------------

class TestLogoutView(TestCase):
    def setUp(self):
        testuser = User.objects.create_user(username="testuser", email="testuser@example.com", password="Wr3{j:J%$2]UH<su-~fdyD~Ky)&&yb&M'.hq\rV%")
        testuser.save()
        

    def test_logout_redirect(self):
        self.client.login(username="testuser", password="Wr3{j:J%$2]UH<su-~fdyD~Ky)&&yb&M'.hq\rV%")
        
        # make sure user is logged in
        response = self.client.get(reverse('logout'))
        
        # check if redirecting
        self.assertEqual(response.status_code, 302)
        
        # check response redirects to correct url
        self.assertRedirects(response, reverse("welcome"))

        # check if user is infact logged out
        response = self.client.get(reverse("profile"))
        self.assertRedirects(response, '/login/?next=/profile/')

class TestSignupView(TestCase):
    
    def test_signup_view_GET(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
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
        testuser.save()

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
        pass


class TestDeleteUserView(TestCase):
    def setUp(self):
        testuser = User.objects.create_user(username="testuser", email="testuser@example.com", password="Wr3{j:J%$2]UH<su-~fdyD~Ky)&&yb&M'.hq\rV%")
        testuser.save()

    def test_delete_user_view_with_logged_in_user_GET(self):
        login = self.client.login(username="testuser", password="Wr3{j:J%$2]UH<su-~fdyD~Ky)&&yb&M'.hq\rV%")
        response = self.client.get(reverse("delete"))

        # check if user is logged in
        self.assertEqual(str(response.context["user"]), "testuser")
        
        # Check if response is a success
        self.assertEqual(response.status_code, 200)

        # Check if correct template is used
        self.assertTemplateUsed(response, "fitness_jerk/delete.html")
    
    def test_delete_user_view_with_logged_in_user_POST(self):
        login = self.client.login(username="testuser", password="Wr3{j:J%$2]UH<su-~fdyD~Ky)&&yb&M'.hq\rV%")
        response = self.client.post(reverse("delete"))

        # check if redirected
        self.assertEqual(response.status_code, 302)

        # check if redirect is correct
        # template use is tested in TestCustomLoginView
        self.assertRedirects(response, reverse("login"))

        # check if user is infact deleted
        self.assertFalse(User.objects.filter(username="testuser").exists())
    
    # 
    def test_delete_view_redirect_with_user_not_logged_in(self):
        response = self.client.get(reverse('delete'))
        self.assertRedirects(response, '/login/?next=/delete/')


# -------------------------------- ANA --------------------------------
    
class ProfileSettingsViewTest(TestCase):

    def setUp(self):
        #set up a user for checking purpose
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user_profile = UserProfile.objects.create(
            user=self.user, 
            weight=70, 
            height=1.75, 
            progress=49, 
            workouts_done=49,
            latest_post="Test content"
        )
        #self.post = Posts.objects.create(member=self.user_profile, post="Test content")
        self.client.login(username='testuser', password='testpassword')

    def test_profile_view(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200) #test status code
        self.assertTemplateUsed(response, 'fitness_jerk/profile.html') #test if the template is correct
        # checks if the info are correct in
        self.assertIn('member', response.context)
        self.assertIn('BMI', response.context)
        self.assertIn('progress', response.context)
        self.assertIn('motivational_msg', response.context)
        self.assertIn('level', response.context)

        self.assertEqual(response.context['BMI'], self.user_profile.bmi) # checks the BMI calculation
        self.assertEqual(response.context['progress'], '54%') #checks if the percentage is correct 
        self.assertEqual(response.context['level'], 'Newbie Bastard') # checks the level if it's the correct one
        self.assertEqual(response.context['motivational_msg'], 'Test content') #checks if the post is created
    

    def test_settings_view(self):
        response = self.client.get(reverse('settings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fitness_jerk/settings.html')
        self.assertIn('profile_form', response.context)
        self.assertIn('profile_pic', response.context)
        self.assertIn('context', response.context)
        self.assertEqual(response.context['context']['BMI'], self.user_profile.bmi)
    

    def test_settings_view_post_valid_form(self):
      
        data = {
            'weight': 75,
            'height': 1.80,
        }
        response = self.client.post(reverse('settings'), data)
        self.user_profile.refresh_from_db()
        self.assertEqual(self.user_profile.weight, 75)
        self.assertEqual(self.user_profile.height, 1.80)


    def test_settings_view_post_no_image(self):
        data = {
            'noimage': 'true'
        }
        response = self.client.post(reverse('settings'), data)
        self.user_profile.refresh_from_db()
        self.assertFalse(self.user_profile.image)

    def test_settings_view_post_avatar(self):
        data = {
            'weight': 75,
            'height': 1.80,
            'avatar': 'superman'
        }
        response = self.client.post(reverse('settings'), data)
        self.user_profile.refresh_from_db()
        self.assertEqual(self.user_profile.image, 'static/superman_lego.jpeg')


# -------------------------------- WISAM ----------------------------------
