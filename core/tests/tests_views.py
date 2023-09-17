from django.test import TestCase


class IndexTest(TestCase):
    def setUp(self):
        self.url = 'http://localhost:8000/'

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200) 
    
    def test_template_usado(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'core/pages/index.html')