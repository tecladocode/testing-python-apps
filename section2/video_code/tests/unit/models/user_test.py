"""
Unit tests for the user model.
"""
from models.user import UserModel
from ..base_test import BaseTest

class UserTest(BaseTest):
    def test_create_user(self):
        user = UserModel('test', 'abcd')

        self.assertEqual(user.username, 'test', "The name of the user after creation does not equal the constructor argument.")
        self.assertEqual(user.password, 'abcd', "The password of the user after creation does not equal the constructor argument.")
    
    def test_crud(self):
        with self.app_context():
            user = UserModel('test', 'abcd')

            self.assertIsNone(UserModel.find_by_username('test'), "Found an user with name 'test' before save_to_db")
            self.assertIsNone(UserModel.find_by_id(1), "Found an user with id '1' before save_to_db")            

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username('test'), "Did not find an user with name 'test' after save_to_db")
            self.assertIsNotNone(UserModel.find_by_id(1), "Did not find an user with id '1' after save_to_db")                        
        