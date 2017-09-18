"""
BaseTest

This class should be the parent class to each system test.
It gives each test a Flask test client that we can use.
"""

from unittest import TestCase
from app import app


class BaseTest(TestCase):
    def setUp(self):
        self.app.testing = True
        self.app = app.test_client
