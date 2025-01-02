from examples import *
import unittest

class TestFunctions(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(
            [is_prime(i) == 1 for i in range(10)],
            [False, False, True, True, False, True, False, True, False, False]
        )

    def test_count_primes(self):
        self.assertEqual(
            [count_primes(i) for i in range(10)],
            [0, 0, 0, 1, 2, 2, 3, 3, 4, 4]
        )

    def test_nth_prime(self):
        self.assertEqual(
            [nth_prime(i) for i in range(10)],
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        )

    def test_Ack(self):
        self.assertEqual(
            Ack(1, 1),
            3
        )

if __name__ == "__main__":
    unittest.main()
