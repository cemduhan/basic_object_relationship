import unittest

from main import add_values_in_dict


class Testing(unittest.TestCase):
    def test_add_values_in_dict_key_test(self):
        sample_dict = {}
        key = 2
        values = [1, 3, 4, 5]
        add_values_in_dict(sample_dict, key, values)
        self.assertIn(key, sample_dict.keys())

    def test_add_values_in_dict_value_test(self):
        sample_dict = {}
        key = 2
        values = [1, 3, 4, 5]
        add_values_in_dict(sample_dict, key, values)
        self.assertIn(key, sample_dict.keys())
        self.assertCountEqual(sample_dict[key], values)


if __name__ == '__main__':
    unittest.main()

