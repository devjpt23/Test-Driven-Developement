import unittest
from calculator import Calculator

class Testing(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_adding_two_numbers(self):
        result = self.calculator.add(20,20)
        self.assertEqual(20+20,result)

        result = self.calculator.add(34.2,2)
        self.assertEqual(34.2+2,result)
    
    def test_adding_two_non_numbers(self):
        self.assertRaises(TypeError,self.calculator.add,'hello','world')
        self.assertRaises(TypeError,self.calculator.add,20,'world')
        self.assertRaises(TypeError,self.calculator.add,'hello',20)
        self.assertRaises(TypeError,self.calculator.add,'60.12.23','world')

    def test_adding_string(self):
        result = self.calculator.add('20','20')
        self.assertEqual(20+20,result)

        result = self.calculator.add('30','20')
        self.assertEqual(30+20,result)

        
if __name__ == '__main__':
    unittest.main()