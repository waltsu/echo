import unittest
import json
import application

class ApplicationTestCase(unittest.TestCase):

  def setUp(self):
    application.app.config['TESTING'] = True
    self.app = application.app.test_client()

  def test_root(self):
    response = self.app.get('/')
    self.assertEqual(response.status_code, 404)

  def test_echoing(self):
    response = self.app.get('/foo')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.get_data(), '{"echo": "foo"}')

if __name__ == '__main__':
  unittest.main()
