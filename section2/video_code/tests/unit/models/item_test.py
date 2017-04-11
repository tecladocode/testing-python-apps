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

    def test_item_json(self):
        item = ItemModel('test', 19.99, 1)

        self.assertEqual(item.json(), {
            'name': 'test',
            'price': 19.99
        })
    
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 19.99, 1)

            self.assertIsNone(ItemModel.find_by_name('test'))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'))
        