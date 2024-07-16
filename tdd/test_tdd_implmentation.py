import unittest
from tdd_implmentation import Writing

class Testing(unittest.TestCase):
    def setUp(self):
        self.writing = Writing()
    
    def test_check_if_output_is_given(self):
        result = self.writing.greeting('Dev')
        self.assertEqual('Hello Dev',result)

        result = self.writing.greeting('Alice')
        self.assertEqual('Hello Alice',result)

        result = self.writing.greeting('Joey')
        self.assertEqual('Hello Joey',result)
    
    def test_writing_non_alpahbets(self):
        with self.assertRaises(ValueError):
            self.writing.greeting(123)

    
    
    

if __name__ == '__main__':
    unittest.main()