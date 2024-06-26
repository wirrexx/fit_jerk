from django.test import TestCase
from django.contrib.auth.models import User
from fitness_jerk.models import Members

class MembersModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        testuser = User.objects.create(username="Testian", email="testian@test.tst", password="Wr3{j:J%$2]UH<su-~fdyD~Ky)&&yb&M'.hq\rV%")
        Members.objects.create(user=testuser)
        userinfo = Members.objects.get(id=1)

    def test_user_label(self):
        userinfo = Members.objects.get(id=1)
        field_label = userinfo._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    def test_height_label(self):
        userinfo = Members.objects.get(id=1)
        field_label = userinfo._meta.get_field("height").verbose_name
        self.assertEqual(field_label, "height")

    def test_progress_label(self):
        userinfo = Members.objects.get(id=1)
        field_label = userinfo._meta.get_field("progress").verbose_name
        self.assertEqual(field_label, "progress")

    def test_workouts_done_label(self):
        userinfo = Members.objects.get(id=1)
        field_label = userinfo._meta.get_field("workouts_done").verbose_name
        self.assertEqual(field_label, "workouts done")

    #Test @property: level
    def test_newbie_bastard_level(self):
        userinfo = Members.objects.get(id=1)
        for workouts_done in range(0,50):
            userinfo.workouts_done = workouts_done
            self.assertEqual(userinfo.level, "Newbie Bastard")
        
    def test_fit_bastard_level(self):
        userinfo = Members.objects.get(id=1)
        for workouts_done in range(50, 100):
            userinfo.workouts_done = workouts_done
            self.assertEqual(userinfo.level, "Fit Bastard")
    
    def test_master_bastard_level(self):
        userinfo = Members.objects.get(id=1)
        for workouts_done in range(100, 150):
            userinfo.workouts_done = workouts_done
            self.assertEqual(userinfo.level, "Master Bastard")

    def test_supreme_bastard_level(self):
        userinfo = Members.objects.get(id=1)
        for workouts_done in range(150, 200):
            userinfo.workouts_done = workouts_done
            self.assertEqual(userinfo.level, "Supreme Bastard")
    
    def test_ultra_bastard_level(self):
        userinfo = Members.objects.get(id=1)
        for workouts_done in range(200, 250):
            userinfo.workouts_done = workouts_done
            self.assertEqual(userinfo.level, "Ultra Bastard")
    
    def test_god_bastard_level(self):
        userinfo = Members.objects.get(id=1)
        for workouts_done in range(250, 2000):
            userinfo.workouts_done = workouts_done
            self.assertEqual(userinfo.level, "God Bastard")
    
    def test_property_level(self):
        userinfo = Members.objects.get(id=1)
        userinfo.workouts_done = 50
        self.assertEqual(userinfo.level, "Fit Bastard")

    def test_calculate_BMI(self):
        userinfo = Members.objects.get(id=1)
        userinfo.weight = 72
        userinfo.height = 1.80
        self.assertEqual(userinfo.calculate_BMI(), 22.22)
    
    def test_bmi_property(self):
        userinfo = Members.objects.get(id=1)
        userinfo.weight = 72
        userinfo.height = 1.80
        self.assertEqual(userinfo.bmi, 22.22)

    
    # def test_first_name_label(self):
    #     author = Members.objects.get(id=1)
    #     field_label = author._meta.get_field('first_name').verbose_name
    #     self.assertEqual(field_label, 'first name')

    # def test_date_of_death_label(self):
    #     author = Members.objects.get(id=1)
    #     field_label = author._meta.get_field('date_of_death').verbose_name
    #     self.assertEqual(field_label, 'died')

    # def test_first_name_max_length(self):
    #     author = Members.objects.get(id=1)
    #     max_length = author._meta.get_field('first_name').max_length
    #     self.assertEqual(max_length, 100)

    # def test_object_name_is_last_name_comma_first_name(self):
    #     author = Members.objects.get(id=1)
    #     expected_object_name = f'{author.last_name}, {author.first_name}'
    #     self.assertEqual(str(author), expected_object_name)

    # def test_get_absolute_url(self):
    #     author = Members.objects.get(id=1)
    #     # This will also fail if the urlconf is not defined.
    #     self.assertEqual(author.get_absolute_url(), '/catalog/author/1')

    # def test_calculate_BMI(self):
    #     pass
