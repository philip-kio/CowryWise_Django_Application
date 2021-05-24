from django.http import response
from django.test import TestCase,Client
from .models import TimeUUID
from django.urls import reverse

from .models import TimeUUID


# Create your tests here.
class ApiViewTest(TestCase):

    def setUp(cls):
        text = 'we'


    def test_list_view(self):
        response = self.client.get(reverse('key_value'))
        self.assertEqual(response.status_code, 200)
        

    def test_create_view(self):
        response = self.client.post(reverse('create'),
        {'text': 'ew'
        })
        self.assertRedirects(response,'/api/v1/',status_code=302,target_status_code=200, fetch_redirect_response=True)
