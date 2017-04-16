from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest
import json


class StoreTest(BaseTest):
    def test_store_not_found(self):
        with self.app() as c:
            r = c.get('/store/test')
            self.assertEqual(r.status_code, 404)

    def test_store_found(self):
        with self.app() as c:
            with self.app_context():
                StoreModel('test').save_to_db()
                r = c.get('/store/test')

                self.assertEqual(r.status_code, 200)
                self.assertDictEqual(d1={'name': 'test', 'items': []},
                                     d2=json.loads(r.data))

    def test_store_with_items_found(self):
        with self.app() as c:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 2.99, 1).save_to_db()
                r = c.get('/store/test')

                self.assertEqual(r.status_code, 200)
                self.assertDictEqual(d1={'name': 'test', 'items': [{'name': 'test', 'price': 2.99}]},
                                     d2=json.loads(r.data))

    def test_delete_store(self):
        with self.app() as c:
            with self.app_context():
                StoreModel('test').save_to_db()
                r = c.delete('/store/test')

                self.assertEqual(r.status_code, 200)
                self.assertDictEqual(d1={'message': 'Store deleted'},
                                     d2=json.loads(r.data))

    def test_create_store(self):
        with self.app() as c:
            with self.app_context():
                r = c.post('/store/test')

                self.assertEqual(r.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name('test'))
                self.assertDictEqual(d1={'name': 'test', 'items': []},
                                     d2=json.loads(r.data))

    def test_create_duplicate_store(self):
        with self.app() as c:
            with self.app_context():
                c.post('/store/test')
                r = c.post('/store/test')

                self.assertEqual(r.status_code, 400)

    def test_store_list(self):
        with self.app() as c:
            with self.app_context():
                StoreModel('test').save_to_db()
                r = c.get('/stores')

                self.assertDictEqual(d1={'stores': [{'name': 'test', 'items': []}]},
                                     d2=json.loads(r.data))

    def test_store_with_items_list(self):
        with self.app() as c:
            with self.app_context():
                StoreModel('test').save_to_db()
                ItemModel('test', 17.99, 1).save_to_db()
                r = c.get('/stores')

                self.assertDictEqual(d1={'stores': [{'name': 'test', 'items': [{'name': 'test', 'price': 17.99}]}]},
                                     d2=json.loads(r.data))
