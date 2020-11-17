'''
Author: your name
Date: 2020-11-16 13:57:51
LastEditTime: 2020-11-16 22:10:08
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \recipe-app-api\app\core\tests\test_admin.py
'''

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@haolin.com',
            password='test1234'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@haolin.com',
            password='test1234',
            name='Test user full name'
        )

    def test_usres_listed(self):
        # Test that users are listed on user page
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        # Test that ther user edit page works
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        
    def test_create_user_page(self):
        # Test the create user page works
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
