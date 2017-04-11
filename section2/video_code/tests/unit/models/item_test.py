"""
Unit tests for the Item model.
"""
from models.item import ItemModel
from ..base_test import BaseTest

class ItemTest(BaseTest):
    def test_create_item(self):
        item = ItemModel('test', 19.99, 1)

        self.assertEqual(item.name, 'test')
