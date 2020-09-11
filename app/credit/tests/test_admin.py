from django.test import TestCase
from django.urls import reverse
from django.test import Client
from django.contrib.auth import get_user_model

class AdminSiteTests(TestCase):

	def setUp(self):
		self.client = Client()
		self.admin_user = get_user_model().objects.create_superuser(username='admin@gmail.com',password='password123')
		self.client.force_login(self.admin_user)

	def test_predictor_list_page(self):
		"""Test that the create user page works"""
		url = reverse('admin:credit_predictor_changelist')
		res = self.client.get(url)

		self.assertEqual(res.status_code, 200)