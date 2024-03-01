import unittest
from asq import query

__author__ = "Sixty North"


class TestAsq(unittest.TestCase):

    def test_asq_iterable(self):
        a = [5, 4, 3, 2, 1]
        b = query(a)

    def test_asq_non_iterable(self):
        self.assertRaises(TypeError, lambda: query(5))



