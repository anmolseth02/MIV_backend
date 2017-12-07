import unittest
from app import app

class IntegerArithmenticTestCase(unittest.TestCase):

# test 1
	def testAdd(self): 
		self.assertEquals((1 + 2), 3)
		self.assertEquals(0 + 1, 1)
# test 2
	def test_two(self):
		tester = app.test_client(self)
		response = tester.get('/')
		self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
	unittest.main()