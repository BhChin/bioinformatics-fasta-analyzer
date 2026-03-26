from calculation import *
import unittest

class TestCalculation(unittest.TestCase):

    def test_calculate_gc(self):
        self.assertEqual(calculate_gc('AAATTTGCGC'), 40)
        self.assertEqual(calculate_gc('GCGC'), 100)
        self.assertEqual(calculate_gc('AAATTTTGCGC'), 4/11*100)

    def test_calculate_at(self):
        self.assertEqual(calculate_at('GGGCCCATAT'), 40)
        self.assertEqual(calculate_at('ATAT'), 100)
        self.assertEqual(calculate_at('ATATGGGGCCC'), 4/11*100)

    def test_find_dimers(self):
        self.assertEqual(find_dimers('ATCG'), {'AT': 1, 'TC': 1, 'CG': 1})
        self.assertEqual(find_dimers('ATCGCG'), {'AT': 1, 'TC': 1, 'CG': 2, 'GC': 1})
        self.assertEqual(find_dimers('ATAT'), {'TA': 1, 'AT': 2})