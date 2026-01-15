import unittest


# def add(a, b):
#     return a + b


# class TestAddFunction(unittest.TestCase):
#     def test_add_positive_numbers(self):
#         self.assertEqual(add(1, 2), 3)

#     def test_add_negative_numbers(self):
#         self.assertEqual(add(-1, -2), -3)

#     def test_add_mixed_numbers(self):
#         self.assertEqual(add(1, 2,), 3)
#         self.assertEqual(add(-1, -2), -3)


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_strings_a(self):
        self.assertEqual('a'*4, 'aaaa')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_strip(self):
        s = 'geeksforgeeks'
        self.assertEqual(s.strip('geek'), 'sforgeeks')

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
