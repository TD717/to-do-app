import unittest
from app import app, todos

class ToDoAppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        todos.clear()  # Clear global list before each test

    def test_homepage_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"My To-Do List", response.data)

    def test_add_task(self):
        self.client.post('/add', data={'todo': 'Test task'})
        self.assertIn('Test task', todos)

    def test_delete_task(self):
        todos.append('Task to delete')
        self.client.post('/delete/0')
        self.assertNotIn('Task to delete', todos)

if __name__ == '__main__':
    unittest.main()
