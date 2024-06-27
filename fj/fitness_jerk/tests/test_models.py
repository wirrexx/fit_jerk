from django.test import TestCase
from django.contrib.auth.models import User
from fitness_jerk.models import UserProfile

class MembersModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        testuser = User.objects.create(username="Testian", email="testian@test.tst", password="Wr3{j:J%$2]UH<su-~fdyD~Ky)&&yb&M'.hq\rV%")
        UserProfile.objects.create(user=testuser)
        userinfo = UserProfile.objects.get(id=1)

    def test_user_label(self):
        userinfo = UserProfile.objects.get(id=1)
        field_label = userinfo._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    def test_height_label(self):
        userinfo = UserProfile.objects.get(id=1)
        field_label = userinfo._meta.get_field("height").verbose_name
        self.assertEqual(field_label, "height")

    def test_progress_label(self):
        userinfo = UserProfile.objects.get(id=1)
        field_label = userinfo._meta.get_field("progress").verbose_name
        self.assertEqual(field_label, "progress")

    def test_workouts_done_label(self):
        userinfo = UserProfile.objects.get(id=1)
        field_label = userinfo._meta.get_field("workouts_done").verbose_name
        self.assertEqual(field_label, "workouts done")

    #Test @property: level
    def test_newbie_bastard_level(self):
        userinfo = UserProfile.objects.get(id=1)
        for workouts_done in range(0,90):
            userinfo.workouts_done = workouts_done
            self.assertEqual(userinfo.level, "Newbie Bastard")
        
    def test_fit_bastard_level(self):
        userinfo = UserProfile.objects.get(id=1)
        for workouts_done in range(90, 180):
            userinfo.workouts_done = workouts_done
            self.assertEqual(userinfo.level, "Fit Bastard")
    
    def test_master_bastard_level(self):
        userinfo = UserProfile.objects.get(id=1)
        for workouts_done in range(180, 270):
            userinfo.workouts_done = workouts_done
            self.assertEqual(userinfo.level, "Master Bastard")

    def test_supreme_bastard_level(self):
        userinfo = UserProfile.objects.get(id=1)
        for workouts_done in range(270, 360):
            userinfo.workouts_done = workouts_done
            self.assertEqual(userinfo.level, "Supreme Bastard")
    
    def test_ultra_bastard_level(self):
        userinfo = UserProfile.objects.get(id=1)
        for workouts_done in range(360, 450):
            userinfo.workouts_done = workouts_done
            self.assertEqual(userinfo.level, "Ultra Bastard")
    
    def test_god_bastard_level(self):
        userinfo = UserProfile.objects.get(id=1)
        for workouts_done in range(450, 2000):
            userinfo.workouts_done = workouts_done
            self.assertEqual(userinfo.level, "God Bastard")
    
    def test_property_level(self):
        userinfo = UserProfile.objects.get(id=1)
        userinfo.workouts_done = 50
        self.assertEqual(userinfo.level, "Newbie Bastard")

    def test_calculate_BMI(self):
        userinfo = UserProfile.objects.get(id=1)
        userinfo.weight = 72
        userinfo.height = 1.80
        self.assertEqual(userinfo.calculate_BMI(), 22.22)
    
    def test_bmi_property(self):
        userinfo = UserProfile.objects.get(id=1)
        userinfo.weight = 72
        userinfo.height = 1.80
        self.assertEqual(userinfo.bmi, 22.22)

    
    