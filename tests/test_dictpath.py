import unittest

from dictpath import dictpath


class TestDictPath(unittest.TestCase):
    def test_explore(self):
        d = { 'level1a': 'string'}
        self.assertEqual(dictpath(d).explore(), { 'level1a': 'str' })

        d = { 'level1a': 'string',
              'level1b': 1,
              'level1c': [1 ,2 ,3],
              }
        self.assertEqual(dictpath(d).explore(), { 'level1a': 'str' ,
                                                  'level1b': 'int' ,
                                                  'level1c[]': ['int']})

        d = { 'level1a': 'string',
              'level1b': 1,
              'level1c': [1 ,2 ,3],
              'level1d': { 'level2': 'string' },
              'level1e': { 'level2': { 'level3': 1 } }
              }
        self.assertEqual(dictpath(d).explore(),
                {
                  'level1a': 'str' ,
                  'level1b': 'int' ,
                  'level1c[]': ['int'],
                  'level1d': { 'level1d/level2': 'str'},
                  'level1e': { 'level1e/level2': { 'level1e/level2/level3': 'int' } }
                })

    def test_path(self):
        d = { 'level1a': 'string',
              'level1b': 1,
              'level1c': [1 ,2 ,3],
              'level1d': { 'level2': 'string' },
              'level1e': { 'level2': { 'level3': 1 } }
              }

        path = { 'a': 'level1a' }
        expected_value = { 'a': 'string' }
        self.assertEqual(dictpath(d).path(path), expected_value)

        path = { 'deep': 'level1e/level2/level3' }
        expected_value = { 'deep': 1 }
        self.assertEqual(dictpath(d).path(path), expected_value)

        #invalid path
        path = { 'a': 'not_exists_path' }
        expected_value = { 'a': None }
        self.assertEqual(dictpath(d).path(path), expected_value)

    def test_query(self):
        d = { 'level1a': 'string',
              'level1b': 1,
              'level1c': [1 ,2 ,3],
              'level1d': [ { 'level2': 'value' }, {'level2': 'other value'} ],
              'level1e': { 'level2': 'anthony' },
              'level1f': { 'level2': { 'level3': 1 } }
              }

        self.assertEqual(dictpath(d).query('level1d'),  [ { 'level2': 'value' }, {'level2': 'other value'} ])
        self.assertEqual(list(dictpath(d).query('level1d/level2')),  ['value', 'other value'])
        self.assertEqual(dictpath(d).query('level1e/level2'), 'anthony')

if __name__ == '__main__':
    unittest.main()
