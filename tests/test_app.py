# import unittest
# from first import app  # Make sure `app` is defined in app/__init__.py or app.py

# class BasicTests(unittest.TestCase):

#     def setUp(self):
#         # Create a test client
#         self.app = app.test_client()
#         self.app.testing = True

#     def test_home_status_code(self):
#         # Assumes your app has a route at '/'
#         response = self.app.get('/')
#         self.assertEqual(response.status_code, 200)

#     def test_home_content(self):
#         # Assumes your home route has a welcome message
#         response = self.app.get('/')
#         self.assertIn(b'Login', response.data)

# if __name__ == "__main__":
#     unittest.main()
import unittest
from first import app  # make sure 'first.py' is in the same directory or in PYTHONPATH

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        response = self.app.get('/')
        self.assertIn(b'Login', response.data)  # Match the content in <h2>Login</h2>

if __name__ == "__main__":
    unittest.main()

