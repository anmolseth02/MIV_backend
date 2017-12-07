import unittest
from main import app

class IntegerArithmenticTestCase(unittest.TestCase):

    def testAdd(self):  ## test method names begin 'test*'
        self.assertEquals((1 + 2), 3)
        self.assertEquals(0 + 1, 1)

if _name_ == '_main_':
    unittest.main()