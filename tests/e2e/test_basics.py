import unittest
import os

os.environ['CONFIG'] = 'Dev'

from flaskApp.main import app

class LoadingTestCase(unittest.TestCase):
    def test_is_main_routing_working(self):

        with app.test_client() as client:

            res = client.get('/')

            self.assertEqual(200, res.status_code)

    def test_is_restapi_routing_working(self):

        with app.test_client() as client:

            res = client.get('/api/hello')

            self.assertEqual(200, res.status_code)

            res = client.get('/api/secret')

            self.assertEqual(401, res.status_code)



if __name__ == '__main__':
    unittest.main()
