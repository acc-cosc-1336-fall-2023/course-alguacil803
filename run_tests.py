import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
#from tests.homework.e_functions import tests_functions
from tests.homework.h_strings import tests_strings
#from tests.homework.d_repetition import tests_repetition

#suite = unittest.TestLoader().loadTestsFromModule(tests_functions)
suite = unittest.TestLoader().loadTestsFromModule(tests_strings)
unittest.TextTestRunner(verbosity=2).run(suite)