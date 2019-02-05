import unittest
from app import app

class TestFibonacci(unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_positive(self):
        response = self.app.get('/fib/0/5')
        self.assertEqual(response.data, 'Please, enter a positive number')

    def test_start_bigger_than_end(self):
        response = self.app.get('/fib/6/3')
        self.assertEqual(response.data, 'The start_idx must be bigger than end_idx')

    def test_successfully_count_fibonacci(self):
        response = self.app.get('/fib/3/5')
        self.assertEqual(response.data, 'Fibonacci sequence: 2, 3, 5')
        self.assertEqual(response.status, '200 OK')

if __name__ == '__main__':
    unittest.main()
