import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
#from tests.examples.i_dictionaries_sets import tests_dictionaries_and_sets
from tests.homework.i_dictionaries_sets import tests_dictionaries_and_sets
#from tests.examples.i_dictionaries_sets import tests_dictionaries_and_sets
from tests.homework.g_lists_and_tuples import tests_lists_and_tuples
#from tests.homework.d_repetition import tests_repetition

suite = unittest.TestLoader().loadTestsFromModule(tests_dictionaries_and_sets)
suite = unittest.TestLoader().loadTestsFromModule(tests_lists_and_tuples)
unittest.TextTestRunner(verbosity=2).run(suite)