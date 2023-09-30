import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''

#from tests.examples.a_example import tests_input_process_output
#from tests.examples.c_decisions import tests_decisions
#from tests.examples.d_repetition import tests_repetition
#from tests.examples.e_functions import tests_functions
#from tests.examples.e_functions import tests_functions
#from tests.examples.f_files_exception import tests_files_exception
#from tests.examples.a_example import tests_input_process_output
#from tests.examples.c_decisions import tests_decisions
#from tests.examples.d_repetition import tests_repetition
#from tests.examples.e_functions import tests_functions
#from tests.examples.e_functions import tests_functions
#from tests.examples.f_files_exception import tests_files_exception
#from tests.examples.g_lists_and_tuples import tests_lists_and_tuples
#from tests.examples.h_strings import tests_strings
#from tests.examples.i_dictionaries_sets import tests_dictionaries_and_sets
#from tests.examples.j_classes_sets import tests_classes
#from tests.examples.k_inheritance import tests_inheritance
#from tests.examples.l_recursion import tests_recursion
#from tests.examples.m_gui import tests_gui
# HOMEWORK 
#from tests.homework.b_in_proc_out import tests_in_proc_out
#from tests.homework.c_decisions import tests_decisions
#from tests.homework.d_repetition import tests_repetition
#from tests.homework.e_functions import tests_functions
from tests.homework.e_functions import tests_functions
#from tests.homework.f_files_exception import tests_files_exception
#from tests.homework.g_lists_and_tuples import tests_lists_and_tuples
#from tests.homework.h_strings import tests_strings

suite = unittest.TestLoader().loadTestsFromModule(tests_functions)
unittest.TextTestRunner(verbosity=2).run(suite)
