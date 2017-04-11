"""
Unit tests for the Item model.
"""
from models.item import ItemModel
from ..base_test import BaseTest

class ItemTest(BaseTest):
    def test_create_item(self):
        # Notice this won't work with PostgreSQL, because of
        # foreign key constraints.
        # The store doesn't exist yet, so it would raise an error.
        # SQLite has no foreign key constraint enforcement, so it works there.
        item = ItemModel('test', 19.99, 1)

        self.assertEqual(item.name, 'test')
        self.assertEqual(item.price, 19.99)
        self.assertEqual(item.store_id, 1)
