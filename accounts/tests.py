# from django.test import TestCase
# from django.contrib.auth.models import User
 
# from django.db.models.signals import post_save  # noqa: F401
# from django.dispatch import receiver  # noqa: F401
# from django.urls import reverse


# class ProfileModelTests(TestCase):

#     def setUp(self):
#         # Create a user instance, which should trigger profile creation
#         self.user = User.objects.create_user(username='testuser', password='testpassword')

#     def test_profile_creation(self):
#         """
#         Test that a Profile instance is created when a new User is saved.
#         """
#         self.assertTrue(Profile.objects.filter(user=self.user).exists(), "Profile was not created for new user.")

#     def test_profile_link_to_user(self):
#         """
#         Test that the created Profile instance is correctly linked to the User instance.
#         """
#         user_profile = Profile.objects.get(user=self.user)
#         self.assertEqual(self.user.profile, user_profile, "User's profile is not linked correctly.")

#     def test_delete_user_cascades_to_profile(self):
#         """
#         Test that deleting a User instance also deletes the associated Profile instance.
#         """
#         user_id = self.user.id
#         self.user.delete()
#         self.assertFalse(Profile.objects.filter(user_id=user_id).exists(), "Profile was not deleted when the User was deleted.")


# class ProfileFormTests(TestCase):

#     def test_phone_field_validation(self):
#         form_data = {'bio': 'Test Bio', 'phone': '+1234567890'}
#         form = ProfileForm(data=form_data)
#         self.assertTrue(form.is_valid())

#     def test_invalid_phone_field_validation(self):
#         form_data = {'bio': 'Test Bio', 'phone': 'invalidphone'}
#         form = ProfileForm(data=form_data)
#         self.assertFalse(form.is_valid())


# class ProfileViewTests(TestCase):

#     def setUp(self):
#         self.user = User.objects.create_user(username='testviewuser', password='password')
#         self.client.login(username='testviewuser', password='password')

#     def test_edit_profile_view(self):
#         response = self.client.get(reverse('accounts:edit_profile'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'form')
