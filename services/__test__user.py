import unittest
import json
from utils.user_util import fetch_users
from user import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_users_list(self):
        response = self.client.get('/users')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, dict)

    def test_get_user_by_id(self):
        # Make a GET request to the '/user/{id}' endpoint
        user_id = '1823a56e-4e83-43a3-ab60-2c8f00209cb6'
        response = self.client.get(f'/user/{user_id}')

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, dict)

    def test_create_user(self):
        # Make a POST request to the '/user' endpoint
        user_data = {
            'email': 'firth11@example.com',
            'first_name': 'firth',
            'last_name': 'manee',
            'password': 'firthpw'
        }
        response = self.client.post('/user', json=user_data)

        # Assert the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Parse the response data as JSON
        data = json.loads(response.data)

        # Assert the data is of type dict
        self.assertIsInstance(data, dict)

        # Assert that the user is created in the data source
        users = fetch_users()  # Assuming fetch_users retrieves the user data from the data source
        created_user = None
        for user in users.values():
            if user['email'] == user_data['email']:
                created_user = user
                break
        self.assertIsNotNone(created_user)
        self.assertEqual(created_user['email'], user_data['email'])
        self.assertEqual(created_user['first_name'], user_data['first_name'])
        self.assertEqual(created_user['last_name'], user_data['last_name'])
        self.assertEqual(created_user['password'], user_data['password'])


if __name__ == '__main__':
    unittest.main()
