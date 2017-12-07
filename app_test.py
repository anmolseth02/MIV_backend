import unittest
from app import app

class IntegerArithmenticTestCase(unittest.TestCase):
	def testAdd(self): 
		self.assertEquals((1 + 2), 3)
		self.assertEquals(0 + 1, 1)


if __name__ == '__main__':
	unittest.main()