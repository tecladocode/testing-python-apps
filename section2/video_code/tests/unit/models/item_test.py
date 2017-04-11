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

        self.assertEqual(item.name, 'test', "The name of the item after creation does not equal the constructor argument.")
        self.assertEqual(item.price, 19.99, "The price of the item after creation does not equal the constructor argument.")
        self.assertEqual(item.store_id, 1, "The store_id of the item after creation does not equal the constructor argument.")
        self.assertIsNone(item.store, "The item's store was not None even though the store was not created.")

    def test_item_json(self):
        item = ItemModel('test', 19.99, 1)
        expected = {
            'name': 'test',
            'price': 19.99
        }

        self.assertEqual(
            item.json(),
            expected,
            "The JSON export of the item is incorrect. Received {}, expected {}.".format(item.json(), expected))
    
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 19.99, 1)

            self.assertIsNone(ItemModel.find_by_name('test'), "Found an item with name 'test' before save_to_db")

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'), "Did not find an item with name 'test' after save_to_db")

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'), "Found an item with name 'test' after delete_from_db")
        