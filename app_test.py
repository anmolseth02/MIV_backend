import unittest
from app import app

class IntegerArithmenticTestCase(unittest.TestCase):
	def testAdd(self): 
		self.assertEquals((1 + 2), 3)
		self.assertEquals(0 + 1, 1)

	def test_two(self):
		tester = app.test_client(self)
		self.assertEquals(tester.get('/').status_code, 200)


if __name__ == '__main__':
	unittest.main()