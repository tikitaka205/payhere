from user.models import User
from .models import Log
from django.urls import reverse
from rest_framework.test import APITestCase

class LogCreateTest(APITestCase):
    """
    로그 테스트 코드
    """
    @classmethod
    def setUpTestData(cls):
        cls.user_data={"email":"test@test.com","password":"!1testtest"}
        cls.log_data={"money":"2000","content":"친구들이랑 제육 사먹음","category":"식비"}
        cls.user=User.objects.create_user('test@test.com','!1testtest')
        cls.log=Log.objects.create(
            author_id=1,
            id=1,
            money=2000,
            content='친구들이랑 제육 사먹음',
            category='식비',
            )

    def setUp(self):
        self.access_token=self.client.post(reverse('token_obtain'), self.user_data).data['access']

    def test_log_post(self):
        response = self.client.post(
            path=reverse('log'),
            data=self.log_data,
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )
        self.assertEqual(response.status_code,200)
    
    def test_log_list(self):
        response = self.client.get(
            path=reverse('log'),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )
        self.assertEqual(response.status_code,200)

    def test_log_put(self):
        response = self.client.put(
            '/log/1/',
            data=self.log_data,
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )
        self.assertEqual(response.status_code,200)

    def test_log_delete(self):
        response = self.client.delete(
            '/log/1/',
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )
        self.assertEqual(response.status_code,204)

    def test_log_detail_get(self):
        response = self.client.get(
            '/log/1/',
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}"
        )
        self.assertEqual(response.status_code,200)

    

    