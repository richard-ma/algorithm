import unittest
import random


class MyTestCase(unittest.TestCase):
    def mySetUp(self):
        self.l_bound, self.u_bound = -10000, 10000
        self.min_array_length, self.max_array_length = 50, 100
        self.random_test_times = 100

    def create_random_array(self):
        return random.sample(
            range(self.l_bound, self.u_bound),
            random.randint(self.min_array_length, self.max_array_length)
        )
