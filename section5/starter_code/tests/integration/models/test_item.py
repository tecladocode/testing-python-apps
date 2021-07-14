from models.item import  ItemModel
from tests.base_test import BaseTest

class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test',19.99)

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))