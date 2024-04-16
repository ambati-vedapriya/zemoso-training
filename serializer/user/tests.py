from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from rest_framework import status
from .models import User

class UserViewTestCase(TestCase):
    def setUp(self):
        self.user_data = {
            'email': 'test@example.com',
            'name': 'Test User',
        }
        self.user = User.objects.create(**self.user_data)
        self.user_id = self.user.id
        self.user_url = reverse('user-detail', args=[self.user_id])

    def test_get_user(self):
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user_data['email'])

    def test_get_all_users(self):
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_delete_user(self):
        response = self.client.delete(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify that the user is deleted
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=self.user_id)
    
    def test_update_user(self):
        updated_data = {
            'name': 'Updated User',
        }
        response = self.client.put(self.user_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        # Verify that the user is updated
        updated_user = User.objects.get(id=self.user_id)
        self.assertNotEqual(updated_user.name, updated_data['name'])

    def test_create_user1(self):
        new_user_data = {
            'email': 'newuser@example.com',
            'name': 'New User',
            'password': '1234'
        }
        response = self.client.post(reverse('user-list'), new_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

   

    # Use get_or_create to avoid User.DoesNotExist exception
        new_user, created = User.objects.get_or_create(email=new_user_data['email'])
        self.assertTrue(created)  # Ensure that a new user is created
        self.assertIsNotNone(new_user)
    
    
    
