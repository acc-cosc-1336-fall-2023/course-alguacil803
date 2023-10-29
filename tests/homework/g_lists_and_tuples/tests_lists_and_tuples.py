import unittest
from src.homework.g_lists_and_tuples.lists import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):
    def test_add_inventory(self):
        inventory_dictionary = {}
        add_inventory(inventory_dictionary, 'Widget1', 10)
        self.assertEqual(inventory_dictionary['Widget1'], 10)
        add_inventory(inventory_dictionary, 'Widget1', 25)
        self.assertEqual(inventory_dictionary['Widget1'], 35)
        add_inventory(inventory_dictionary, 'Widget1', -10)
        self.assertEqual(inventory_dictionary['Widget1'], 25)
        self.assertEqual(inventory_dictionary, {'Widget1':25})

    def test_remove_from_inventory(self):
        inventory_dictionary = {'Widget1': 32, 'Widget2': 29}
        self.assertEqual(len(inventory_dictionary), 2)
        self.assertEqual(remove_inventory_widget(inventory_dictionary, 'Widget1'), 'Record Deleted')
        self.assertEqual(len(inventory_dictionary), 1)
        self.assertEqual(remove_inventory_widget(inventory_dictionary, 'Widget1'), "Item Not Found")
        self.assertEqual(inventory_dictionary, {'Widget2': 29})
        print(inventory_dictionary)