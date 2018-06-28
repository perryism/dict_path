import unittest

from dictpath.jsonpath import jsonpath

class TestJsonPath(unittest.TestCase):
    def test_explore(self):
        js = {
            "keys": [
                {
                    "item1": 1,
                    "item2": 2
                },
                {
                    "item1": 3,
                    "item2": 4
                },
                {
                    "item1": 5,
                    "item2": 6
                }
            ]
        }
        self.assertEqual(jsonpath(js).query("item2"), [{"item2": 2},
            {"item2":4}, {"item2": 6}])

    def test_path(self):
        d = { 'level1a': 'string',
              'level1b': 1,
              'level1c': [1 ,2 ,3],
              'level1d': { 'level2': 'string' },
              'level1e': { 'level2': { 'level3': 1 } }
              }

        path = { 'a': 'level1a' }
        expected_value = { 'a': 'string' }
        #self.assertEqual(dictpath(d).path(path), expected_value)

        path = { 'deep': 'level1e/level2/level3' }
        expected_value = { 'deep': 1 }
        #self.assertEqual(dictpath(d).path(path), expected_value)

        #invalid path
        path = { 'a': 'not_exists_path' }
        expected_value = { 'a': None }
        #self.assertEqual(dictpath(d).path(path), expected_value)

if __name__ == '__main__':
    unittest.main()
