import unittest
from newUnittest import calculations

class Testing(unittest.TestCase):
    def setUp(self):
        self.calulation = calculations()

    def test_checking_if_output(self):
        result = self.calulation.multiply(2,2)
        self.assertEqual(2*2,result)

    def test_multiplying_no_non_numbers(self):
        with self.assertRaises(TypeError):
            self.calulation.multiply('2','2')
        
    def test_multiply_with_string(self):
        with self.assertRaises(TypeError):
            self.calulation.multiply('dev','patel')
            self.calulation.multiply('dev','2')
            self.calulation.multiply('2','patel')
            # self.calulation.multiply('2.2','2.2')
            # self.calulation.multiply('2.2.2','2.2.2')


if __name__=='__main__':
    unittest.main()