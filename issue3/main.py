from one_hot_encoder import fit_transform
import unittest


class TestFitTransform(unittest.TestCase):
    def test_moscow(self):
        actual = fit_transform('Moscow')
        expected = [('Moscow', [1])]
        self.assertEqual(actual, expected)

    def test_not_equal(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        actual = fit_transform(cities)
        expected = [
            ('Moscow', [1, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertNotEqual(actual, expected)

    def test_not_in(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        actual = fit_transform(cities)[0]
        expected = [
            ('Moscow', [1, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertIn(actual, expected)

    def test_empty(self):
        self.assertEqual(fit_transform(''), [('', [1])])

    def test_error_raise(self):
        self.assertRaises(Exception, fit_transform())


if __name__ == '__main__':
    unittest.main()
