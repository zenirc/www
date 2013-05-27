from django.utils import unittest
from lib import schema


class TestSchema(unittest.TestCase):

    def setUp(self):
        self.schema = {
            'author': 'me',
            'name': 'some package',
            'homepage': 'http://mysite',
            'scripts': {
                'start': 'node ./mypackage.js'
            }
        }

    def test_good_schema(self):
        valid, errors = schema.validate(self.schema)
        self.assertTrue(valid)
        self.assertFalse(errors)

    def test_missing_top_level_property(self):
        for prop in self.schema.keys():
            del self.schema[prop]
            valid, errors = schema.validate(self.schema)
            self.assertFalse(valid)
            self.assertEqual(len(errors), 1)
            self.assertIn(prop, errors[0])
            self.setUp()

    def test_missing_start_script(self):
        del self.schema['scripts']['start']
        valid, errors = schema.validate(self.schema)
        self.assertFalse(valid)
        self.assertEqual(len(errors), 1)
        self.assertIn('start', errors[0])
