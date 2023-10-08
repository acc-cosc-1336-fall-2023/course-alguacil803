import unittest

from src.homework.h_strings.strings import get_hamming_distance, get_dna_complement

class Test_Config(unittest.TestCase):

    def test_get_hamming_distance(self):
        self.assertEqual(7, get_hamming_distance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'))

    def test_get_dna_complement(self):
        self.assertEqual('ACCGGGTTTT', get_dna_complement('AAAACCCGGT'))