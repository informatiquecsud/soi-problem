import unittest
import os
import sys

sys.path.append('src')

from main import main

class MainTest(unittest.TestCase):
    
    def setUp(self):
        ...
        
    @classmethod
    def setUpClass(cls):
        ...
        
    def test_main(self):
        self.assertTrue(main())

    
if __name__ == "__main__":
    unittest.main()
