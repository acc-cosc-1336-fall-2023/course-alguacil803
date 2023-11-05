import unittest

from src.homework.i_dictionaries_sets.dictionary import get_p_distance, get_p_distance_matrix

baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah']) 

class Test_Config(unittest.TestCase):

    def test_get_p_distance(self):
        list1 = ['T','T','T','C','C','A','T','T','T','A']
        list2 = ['G','A','T','T','C','A','T','T','T','C']
        self.assertEqual(0.4, get_p_distance(list1, list2))

    def test_p_distance_matrix(self):
        list1 = ['T','T','T','C','C','A','T','T','T','A']
        list2 = ['G','A','T','T','C','A','T','T','T','C']
        list3 = ['T','T','T','C','C','A','T','T','T','T']
        list4 = ['G','T','T','C','C','A','T','T','T','A']
        dataset = [list1, list2, list3, list4]
        self.assertEqual([[0.0, 0.4, 0.1, 0.1], [0.4, 0.0, 0.4, 0.3], [0.1, 0.4, 0.0, 0.2], [0.1, 0.3, 0.2, 0.0]], get_p_distance_matrix(dataset))

class TestSetOperations(unittest.TestCase):
    def setUp(self):
        self.baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        self.basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

    def test_intersection(self):
        intersection_result = self.baseball.intersection(self.basketball)
        expected_intersection = {'Carmen', 'Alicia'}
        self.assertEquals(intersection_result, expected_intersection)

    def test_union(self):
        union_result = self.baseball.union(self.basketball)
        expected_union = {'Jodi', 'Carmen', 'Aida', 'Alicia', 'Eva', 'Sarah'}
        self.assertEquals(union_result, expected_union)

    def test_difference_baseball(self):
        difference_result = self.baseball.difference(self.basketball)
        expected_difference = {'Jodi', 'Aida'}
        self.assertEquals(difference_result, expected_difference)

    def test_difference_basketball(self):
        difference_result = self.basketball.difference(self.baseball)
        expected_difference = {'Eva', 'Sarah'}
        self.assertEquals(difference_result, expected_difference)

    def test_symmetric_difference(self):
        symmetric_difference_result = self.baseball.symmetric_difference(self.basketball)
        expected_symmetric_difference = {'Jodi', 'Eva', 'Aida', 'Sarah'}
        self.assertEquals(symmetric_difference_result, expected_symmetric_difference)