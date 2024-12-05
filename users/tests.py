from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class UserRegistrationTest(TestCase):

    def test_register_user(self):
        response = self.client.post(reverse('register'), {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        })
        self.assertEqual(response.status_code, 200)

    def test_login_user(self):
        User.objects.create_user(username='testuser', password='testpassword123')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword123',
        })
        self.assertEqual(response.status_code, 302)

    def test_logout_user(self):
        User.objects.create_user(username='testuser', password='testpassword123')
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)


class GameMechanicsTest(TestCase):

    def setUp(self):
        pass

    def test_collect_puzzle(self):
        pass

    def test_correct_building_selection(self):
        pass
