from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Todo 

LOCAL_HOST_URL="http://127.0.0.1:8000"

class TodoAPITests(APITestCase):

    def setUp(self):
        """
        Setup the user and url data for the tests:
        """
        # Create a user for login purposes
        self.user = get_user_model().objects.create_user(
            username="duchungtest", password="hung1234@"
        )
        
        # get token for authentication
        self.login_url = LOCAL_HOST_URL + reverse('get_access_token')
        self.refresh_url = LOCAL_HOST_URL + reverse('token_refresh')

        # Todo item endpoints
        self.todo = Todo.objects.create(title="Test Todo", description="Test description", user_id=self.user)
        self.create_url = LOCAL_HOST_URL + reverse('create_Todo_item')
        self.list_url = LOCAL_HOST_URL + reverse('list_Todo_items')
        self.update_url = LOCAL_HOST_URL + reverse('update_Todo_item', args=[self.todo.pk])
        self.delete_url = LOCAL_HOST_URL + reverse('delete_Todo_item', args=[self.todo.pk])
        

    #test login 
    def test_authenticate(self):
        
        response = self.client.post(self.login_url, data={
            'username': 'duchungtest',
            'password': 'hung1234@',
        })
       
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data
    

    # test refresh token
    def test_token_refresh(self):
        
        token = self.test_authenticate()

        # Refresh the token
        response = self.client.post(self.refresh_url, {
            'refresh': token['refresh']
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    # test create todo item
    def test_create_Todo_item(self):
        
        token = self.test_authenticate()
        access_token = token['access']
        title = 'New Todo'
        des = 'New description'
        response = self.client.post(self.create_url,{
            'title': title,
            'description': des,
        }, HTTP_AUTHORIZATION=f'Bearer {access_token}')
        print("`````````````````",response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Todo')


    # test api list
    def test_list_todo_items(self):
        token = self.test_authenticate()
        access_token = token['access']

        response = self.client.get(self.list_url, HTTP_AUTHORIZATION=f'Bearer {access_token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    # test api detail
    def test_get_todo_detail(self):
        token = self.test_authenticate()
        access_token = token['access']

        response = self.client.get(reverse('detail_Todo_item', args=[self.todo.id]), HTTP_AUTHORIZATION=f'Bearer {access_token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.todo.title)

    # test update api
    def test_update_todo_item(self):
        token = self.test_authenticate()
        access_token = token['access']

        updated_title = "Updated Todo Title"
        updated_des = "hellooooooo"

        response = self.client.put(reverse('update_Todo_item', args=[self.todo.id]), {
            'title': updated_title,
            'description': updated_des,
        }, HTTP_AUTHORIZATION=f'Bearer {access_token}')
        print('-----------', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], updated_title)


    # test delete api
    def test_delete_todo_item(self):
        token = self.test_authenticate()
        access_token = token['access']

        response = self.client.delete(reverse('delete_Todo_item', args=[self.todo.id]), HTTP_AUTHORIZATION=f'Bearer {access_token}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(reverse('detail_Todo_item', args=[self.todo.id]), HTTP_AUTHORIZATION=f'Bearer {access_token}')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

