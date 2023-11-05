import dictionary as d

list1 = ['T','T','T','C','C','A','T','T','T','A']
list2 = ['G','A','T','T','C','A','T','T','T','C']
list3 = ['T','T','T','C','C','A','T','T','T','T']
list4 = ['G','T','T','C','C','A','T','T','T','A']

dataset = [list1, list2, list3, list4]

d.print_clean_matrix(d.get_p_distance_matrix(dataset))

d.main_menu()