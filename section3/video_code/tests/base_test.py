"""
BaseTest

This class should be the parent class to each unit test.
It allows for instantiation of the database dynamically,
and makes sure that it is a new, blank database each time.
"""

from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):
    SQLALCHEMY_DATABASE_URI = "sqlite://"

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = BaseTest.SQLALCHEMY_DATABASE_URI
        with app.app_context():
            db.init_app(app)
            db.create_all()
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()
