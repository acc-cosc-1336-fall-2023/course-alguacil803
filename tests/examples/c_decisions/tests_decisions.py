import unittest

#from src.examples.c_decisions.decisions import get_and_result, get_notted_value, get_or_result, is_consonant, is_even, is_odd, is_overtime, is_vowel, test_config
from src.examples.c_decisions.decisions import get_and_result, get_letter_grade, get_notted_value, get_or_result, is_consonant, is_even, is_odd, is_overtime, is_vowel, test_config

class Test_Config(unittest.TestCase):


        

        def test_get_letter_grade(self):
         self.assertEqual(get_letter_grade(105), "Invalid Grade")
         self.assertEqual(get_letter_grade(100), "A")
         self.assertEqual(get_letter_grade(95), "A")
         self.assertEqual(get_letter_grade(90), "A")
         self.assertEqual(get_letter_grade(85), "B")
         self.assertEqual(get_letter_grade(75), "C")
         self.assertEqual(get_letter_grade(65), "D")
         self.assertEqual(get_letter_grade(55), "F")
         self.assertEqual(get_letter_grade(-5), "Invalid Grade")