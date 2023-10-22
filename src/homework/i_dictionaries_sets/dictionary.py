acceptable_characters = ['G','A','T','C']
exit_clause = 'EXIT'
stop_clause = 'STOP'
new_clause = 'NEW'
empty_clause = 'EMPTY'
confirmation_clause = 'YES'
stored_matrix = []
stored_pD_matrix = []

def exit_confirmation(user_confirmation):
    global exit_clause, confirmation_clause

    user_confirmation = input('want to exit? Enter [YES], all different selection return you to the menu.\n\t>>> ').upper()
    if is_confirmed_clause(user_confirmation) == True:
        result = exit_clause
        print('\x1B[3m' + ' Exit  Menu' + '\x1B[0m')
    else: result = 0    
    return result

def is_same_length(s1, s2):
    length_1 = len(s1)
    length_2 = len(s2)
    return length_1 == length_2

def is_acceptable_character(s1):
    global acceptable_characters
    return s1 in acceptable_characters

def is_exit_clause(str):
    str = str.upper()
    global exit_clause
    return str == exit_clause or str == exit_clause[0:1:1] or str == exit_clause[0:2:1] or str == exit_clause[0:3:1] 

def is_stop_clause(str):
    str = str.upper()
    global stop_clause
    return str == stop_clause or str == stop_clause[0:1:1] or str == stop_clause[0:2:1] or str == stop_clause[0:3:1]

def is_new_clause(str):
    str = str.upper()
    global new_clause
    return str == new_clause or str == new_clause[0:1:1] or str == new_clause[0:2:1]

def is_empty_clause(str):
    str = str.upper()
    global empty_clause
    return str == empty_clause or str == empty_clause[0:1:1] or str == empty_clause[0:2:1] or str == empty_clause[0:3:1] or str == empty_clause[0:4:1]

def is_confirmed_clause(str):
    str = str.upper()
    global confirmation_clause
    return str == confirmation_clause or str == confirmation_clause[0:1:1] or str == confirmation_clause[0:2:1]

def make_matrix():
    global stored_matrix, confirmation_clause, stop_clause
    current_list = []
    user_entry = '0'

    while is_stop_clause(user_entry) == False:

        user_entry = input('make an entry:\n  [' + ''.join(acceptable_characters) + ']   to enter a character\n  [new]    to store list and begin a new list\n  [empty]  to clear current list\n  [stop]   to return to main menu \n\t>>> ').upper()

        while is_acceptable_character(user_entry) == True:
            current_list.append(user_entry)
            print(current_list)
            current_list_length = len(current_list)
            print('  Your current list length is: ', current_list_length)
            user_entry = input('Please enter a character from [' + ''.join(acceptable_characters) + '], [new] begin a new list, [empty] to clear current list, or [stop] to end \n\t>>> ').upper()

        if is_new_clause(user_entry) == True:
            print('Your current list is:')
            print(current_list)
            current_list_length = len(current_list)
            print('Total length is:', current_list_length, 'characters.')
            user_confirmation = input('Would you like begin a new list? [YES], or any other response to cancel.\n\t>>> ').upper()
            if is_confirmed_clause(user_confirmation) == True:
                stored_matrix.append(current_list)
                current_list = []
            else:
                print('  >>>CANCEL<<<')
            user_entry = '0'

        elif is_empty_clause(user_entry) == True:
            print('Your current list is:')
            print(current_list)
            print('Total length is:', current_list_length, 'characters.')
            user_confirmation = input('begin a new list? [YES], or any other response to cancel.\n\t>>> ').upper()
            if is_confirmed_clause(user_confirmation) == True:
                current_list = []
            else:
                print('  >>>CANCEL<<<')

        elif is_stop_clause(user_entry) == True:
            user_entry = input('return to main menu?\n\t>>> ').upper()
            if is_confirmed_clause(user_entry) == True:
                user_entry = stop_clause

        else:
            print('  >>>Bad ENTRY<<<')

def main_menu():
    global exit_clause, confirmation_clause, stored_matrix
    user_selection = '0'

    while user_selection != exit_clause:

        user_selection = input(' ' + "\x1B[4m" + 'Homework  Menu:' + "\x1B[0m" + '\n  Press [A] to create your matrix\n  Press [B] for P Distance\n  Type  [exit] to EXIT the program\n\t>>> ')

        if user_selection == 'A':
            make_matrix()

        elif user_selection == 'B':
            print('Your current matrix is: ')
            print_clean_matrix(stored_matrix)
            print('While the P distance is: ')
            print_clean_matrix(get_p_distance_matrix(stored_matrix))

        elif is_exit_clause(user_selection) == True:
            user_selection = exit_confirmation(user_selection)

        else:
            print('  >>>INVALID ENTRY<<<')

def get_p_distance(s1, s2):
    if is_same_length(s1, s2) == True:
        stop_length = len(s1)
        dP = 0
        stop = 0      
        for n in range(stop_length):
            s1[n] = s1[n].upper()
            s2[n] = s2[n].upper()
            if not(is_acceptable_character(s1[n])) or not(is_acceptable_character(s1[n])):
                stop = 1
            elif s1[n] != s2[n] and stop != 1:
                dP += 1
        if stop != 0:        
            return 'Invalid use only utilize A, G, C, or T for the DNA bases.'
        else:
            dP = dP/stop_length
            return dP     
    else: return 'match string length.'

def get_p_distance_matrix(matrix):
    global stored_pD_matrix
    stop_length = len(matrix)

    for n in range(stop_length):
        current_list = []
        for i in range(stop_length):
            #dP = "{:.5f}".format(round(get_p_distance(list[n], list[i]), 5)) #significant digits format
            dP = get_p_distance(matrix[n], matrix[i])
            current_list.append(dP)
        stored_pD_matrix.append(current_list)
    return stored_pD_matrix

def print_clean_matrix(matrix):
    matrix_length = len(matrix)
    for n in range(matrix_length):
        print(matrix[n])