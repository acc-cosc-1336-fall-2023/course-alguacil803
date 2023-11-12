import unittest, random
from src.homework.j_classes.class_a import Die
class Test_Config(unittest.TestCase):

    def test_die(self):
        dice = Die()
        for _ in range(3):
            dice.roll()
            dice_value = dice.get_role_value()
            self.assertEqual(1<= dice_value <= 6 , True)