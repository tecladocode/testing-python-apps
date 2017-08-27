from unittest import TestCase
from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test content')

        self.assertEqual('Test', p.title)
        self.assertEqual('Test content', p.content)

    def test_json(self):
        p = Post('Test', 'Test content')

        self.assertDictEqual({'title': p.title, 'content': p.content}, p.json())
