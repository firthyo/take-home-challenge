import unittest
from flask import Flask
from order import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_user_orders(self):
        user_id = '75397119-64e3-4332-b30d-30ef568e5b06'
        response = self.app.get(f'/user/{user_id}/orders/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, dict)
        self.assertIn('page', data)
        self.assertEqual(data['page'], 1)
        self.assertIn('per_page', data)
        self.assertIn('total_data', data)
        self.assertIn('data', data)

    def test_get_wrong_user_orders(self):
        user_id = '123'
        response = self.app.get(f'/user/{user_id}/orders/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, dict)
        self.assertIn('data', data)
        self.assertEqual(data['data'], [])
        self.assertIn('page', data)
        self.assertEqual(data['page'], 1)
        self.assertIn('per_page', data)
        self.assertIn('total_data', data)
  

    def test_get_order_items(self):
        user_id = '54f8fef0-1707-4b91-b9a8-84caac95da21'
        response = self.app.get(f'/user/{user_id}/order_items/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, dict)
        self.assertIn('page', data)
        self.assertEqual(data['page'], 1)
        self.assertIn('per_page', data)
        self.assertIn('total_data', data)
        self.assertIn('data', data)

    def test_get_order_items_check_correct_len(self):
        user_id = '54f8fef0-1707-4b91-b9a8-84caac95da21'
        response = self.app.get(f'/user/{user_id}/order_items/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, dict)
        self.assertIn('page', data)
        self.assertEqual(data['page'], 1)
        self.assertIn('per_page', data)
        self.assertIn('total_data', data)
        self.assertIn('data', data)
        self.assertGreaterEqual(len(data['data']), 1)

if __name__ == '__main__':
    unittest.main()
