#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import get_person_category
from src.question_b.question_b import get_fahrenheit
from src.question_c.question_c import get_bonus_pay_amount
from src.question_d.question_d import get_day_of_week

class Test_Config(unittest.TestCase):

    def test_question_a(self):
        self.assertEqual(get_person_category(1), 'Infant')
        self.assertEqual(get_person_category(2), 'Child')
        self.assertEqual(get_person_category(14), 'Teenager')
        self.assertEqual(get_person_category(20), 'Adult')
        self.assertEqual(get_person_category(-1), 'Invalid Number')
        self.assertEqual(get_person_category(126), 'Invalid Number')

    def test_question_b(self):
        self.assertEqual(get_fahrenheit(0), 32)
        self.assertEqual(get_fahrenheit(5), 41)
        self.assertEqual(get_fahrenheit(10), 50)
        
    def test_question_c(self):
        self.assertEqual(get_bonus_pay_amount(-1), "Invalid Arguments")
        self.assertEqual(get_bonus_pay_amount(200), 10)
        self.assertEqual(get_bonus_pay_amount(600), 36)
        self.assertEqual(get_bonus_pay_amount(1000), 70)
        self.assertEqual(get_bonus_pay_amount(1500), 120)
        self.assertEqual(get_bonus_pay_amount(2000), "Invalid Arguments")
        
    def test_question_d(self):
        self.assertEqual(get_day_of_week(0),'Invalid Number')
        self.assertEqual(get_day_of_week(1),'Monday')
        self.assertEqual(get_day_of_week(2),'Tuesday')
        self.assertEqual(get_day_of_week(3),'Wednesday')
        self.assertEqual(get_day_of_week(4),'Thursday')
        self.assertEqual(get_day_of_week(5),'Friday')
        self.assertEqual(get_day_of_week(6),'Saturday')
        self.assertEqual(get_day_of_week(7),'Sunday')
        self.assertEqual(get_day_of_week(8),'Invalid Number')