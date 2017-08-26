from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            store = StoreModel('test')
            store.save_to_db()
            item = ItemModel('test', 19.99, 1)

            self.assertIsNone(ItemModel.find_by_name('test'), "Found an item with name 'test' before save_to_db")

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'),
                                 "Did not find an item with name 'test' after save_to_db")

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'), "Found an item with name 'test' after delete_from_db")

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('test_store')
            item = ItemModel('test', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, 'test_store')
