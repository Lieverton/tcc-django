from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tcc.core.models import Articles


class ArticleTest(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('articles')
        data = {'title': 'Test',
                'text': 'Lorem Ipsum',
                'hashtags': '1'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Articles.objects.count(), 1)
        self.assertEqual(Articles.objects.get().title, 'Test')
        self.assertEqual(Articles.objects.get().text, 'Lorem Ipsum')
        self.assertEqual(Articles.objects.get().genre, 'test')
        self.assertEqual(Articles.objects.get().hashtags, 'test')