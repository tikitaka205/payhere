from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import User

class UserRegistrationTest(APITestCase):
    """
    회원가입
    """
    def test_registration(self):
        url=reverse("user")
        user_data={
            "email":"test@test.com",
            "password":"!1testtest"
        }
        response = self.client.post(url, user_data)
        print(response)
        self.assertEqual(response.status_code,201)

class LoginUserTest(APITestCase):
    """
    로그인 테스트코드
    """
    def setUp(self):
        self.data={'email':'test@test.com','password':'!1testtest'}
        self.user=User.objects.create_user('test@test.com','!1testtest')

    def test_login(self):
        response=self.client.post(reverse('token_obtain'),self.data)
        self.assertEqual(response.status_code,200)
