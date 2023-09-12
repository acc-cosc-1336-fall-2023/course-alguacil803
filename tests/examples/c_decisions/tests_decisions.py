from msilib.schema import SelfReg
from typing import Self
import unittest

from src.examples.c_decisions.decisions import get_and_result, get_or_result, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

        def test_and_truth_table(self):
            self.assertEqual(True, get_and_result)(True, True)
            self.assertEqual(False, get_and_result)(True, False)
            self.assertEqual(False, get_and_result)(False, True)
            self.assertEqual(False, get_or_result)(True, True)


