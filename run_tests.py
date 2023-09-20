import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
#from tests.homework.c_decisions import tests_decisions 
##from tests.homework.b_in_proc_out import tests_in_proc_out
#from tests.homework.b_in_proc_out import tests_in_proc_out
#from tests.examples.a_example import tests_devprocess
#from tests.examples.c_decisions import tests_decisions
#from tests.examples.c_decisions import tests_decisions
from tests.examples.c_decisions import tests_decisions

suite = unittest.TestLoader().loadTestsFromModule(tests_decisions)
#suite = unittest.TestLoader().loadTestsFromModule(tests_in_proc_out)


unittest.TextTestRunner(verbosity=2).run(suite)
