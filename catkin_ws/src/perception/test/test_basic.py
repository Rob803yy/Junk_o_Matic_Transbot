#!/usr/bin/env python3
import os
import unittest

class BasicTest(unittest.TestCase):
    def test_read_sample(self):
        path = os.path.join(os.path.dirname(__file__), "sample_data.txt")
        with open(path) as f:
            data = f.read().strip()
        self.assertEqual(data, "sample data")

if __name__ == '__main__':
    import rostest
    rostest.rosrun('perception', 'basic_test', BasicTest)
