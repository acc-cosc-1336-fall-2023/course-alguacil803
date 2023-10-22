import unittest
'''

'''

from tests.examples.g_lists_and_tuples import tests_lists_and_tuples


from tests.homework.i_dictionaries_sets import tests_dictionaries_and_sets
#from tests.homework.j_classes_sets import tests_classes
#from tests.homework.k_inheritance import tests_inheritance
#from tests.homework.l_recursion import tests_recursion
#from tests.homework.m_gui import tests_gui

suite = unittest.TestLoader().loadTestsFromModule(tests_lists_and_tuples)
suite = unittest.TestLoader().loadTestsFromModule(tests_dictionaries_and_sets)
unittest.TextTestRunner(verbosity=2).run(suite)