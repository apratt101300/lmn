import tempfile
import filecmp
import os

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User 
from django.db import IntegrityError
from django.utils import timezone
import pytz
timezone.now()

from ..models import Show

# Create your tests here.


class TestUser(TestCase):

    def test_create_user_duplicate_username_fails(self):

        user = User(username='bob', email='bob@bob.com', first_name='bob', last_name='bob')
        user.save()

        user2 = User(username='bob', email='another_bob@bob.com', first_name='bob', last_name='bob')
        with self.assertRaises(IntegrityError):
            user2.save()


    def test_create_user_duplicate_email_fails(self):
        user = User(username='bob', email='bob@bob.com', first_name='bob', last_name='bob')
        user.save()

        user2 = User(username='bob', email='bob@bob.com', first_name='bob', last_name='bob')
        with self.assertRaises(IntegrityError):
            user2.save()


class TestShow(TestCase):

    fixtures = ['testing_users', 'testing_artists', 'testing_venues']
   
    def test_create_new_show(self):
        pass
        