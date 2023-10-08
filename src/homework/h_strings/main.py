import strings


dna1 = 'GAGCCTACT'
dna2 = 'CATCGTAAT'


dna3 = 'AAAACCCGGT'

"""
A-Hamming Distance
B-Dna Complement
C-Exit
The program runs until the user chooses option C.

Option A prompt the user for a string, call the get_hamming_distance function and display the result.
Option B prompt the user for a string, call the get_dna_complement function and display the result.
"""


"""
print(strings.get_hamming_distance(dna1, dna2))

print(strings.get_dna_complement(dna1))
"""

exit_clause = 'C'
confirmation = 'YES'
user_selection = '0'

while user_selection != exit_clause:
    user_selection = input(' ' + "\x1B[4m" + 'Homework 5 Menu:' + "\x1B[0m" + '\n  Press [A] for Hamming Distance\n        [B] for Dna Complement\n        [C] to  Exit the program\n\t>>> ')
    if user_selection == 'A':
        print(' Your Hamming Distance for:\n ' + dna1 + ' and\n ' + dna2 + ' is:', strings.get_hamming_distance(dna1, dna2))
        user_selection = strings.exit_confirmation_loop(user_selection)
    elif user_selection == 'B':
        print(' Your DNA Complement for:\n ' + dna3 + '\tis\n', strings.get_dna_complement(dna3))
        user_selection = strings.exit_confirmation_loop(user_selection)
    elif user_selection == 'C':  
        user_selection = strings.exit_confirmation_loop(user_selection)
    else: 
        print(' Invalid Value.')
        user_selection = strings.exit_confirmation_loop(user_selection)