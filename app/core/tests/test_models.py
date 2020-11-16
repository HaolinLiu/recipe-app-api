'''
Author: your name
Date: 2020-11-16 13:01:26
LastEditTime: 2020-11-16 13:55:55
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \recipe-app-api\app\core\tests\test_models.py
'''
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        # Test creating a new user with an email is successful
        email = 'test@haolin.com'
        password = "testpass"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        # Test the email for a new user is normalized
        email = 'test@HAOLIN.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        # Test creating user with no email raises error
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        # Test creating a new superuser
        user = get_user_model().objects.create_superuser(
            'test@haolin.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
