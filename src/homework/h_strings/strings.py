Valid_characters = ['G','A','T','C']

def determine_same_length(dna1, dna2):
    length_1 = len(dna1)
    length_2 = len(dna2)
    result = '0'
    if length_1 != length_2: result = 'FALSE'
    else: result = 'TRUE'
    return result

def get_hamming_distance(dna1, dna2):
    if determine_same_length(dna1, dna2) == 'TRUE':
        dna1 = dna1.upper()
        dna2 = dna2.upper()
        stop_length = len(dna1)
        dH = 0
        stop = 0      
        for n in range(stop_length):
            if dna1[n] not in Valid_characters or dna2[n] not in Valid_characters:
                stop = 1
            elif (dna1[n] != dna2[n]) and stop != 1:
                dH += 1
        if stop != 0:        
            return 'Invalid character please only utilize AGCT for the DNA bases.'
        else: return dH     
    else: return 'Please correct the lengths of your DNA examples to match.'

def get_dna_complement(dna1):
        dna1 = dna1.upper()
        stop_length = len(dna1)
        dc = ''
        n_complement = 0
        stop = 0
        for n in range(stop_length):
            n_complement = stop_length - n - 1
            if dna1[n_complement] not in Valid_characters:
                stop = 1
            elif stop != 1:
                if dna1[n_complement] == 'G': dc += 'C'
                elif dna1[n_complement] == 'C': dc += 'G'
                elif dna1[n_complement] == 'A': dc += 'T'
                elif dna1[n_complement] == 'T': dc += 'A'
        if stop != 0:        
            return 'Invalid character please only utilize AGCT for the DNA bases.'
        else: return dc

def exit_confirmation_loop(user_confirmation):
    exit_clause = 'C'
    confirmation = 'YES'

    if user_confirmation != exit_clause:
        
        user_confirmation = input(' Press to exit? [YES/NO] ')
        if user_confirmation.upper() == confirmation or user_confirmation.upper() == confirmation[0:1:1] or user_confirmation.upper() == confirmation[0:2:1]:
            
            user_confirmation = input(' you want to exit? Enter [YES], all other selections will return you to the menu.\n\t>>> ')
            if user_confirmation.upper() == confirmation or user_confirmation.upper() == confirmation[0:1:1] or user_confirmation.upper() == confirmation[0:2:1]:
                result = exit_clause
                print('\x1B[3m' + ' Exiting the Homework 5 Menu' + '\x1B[0m')
            
            else: result = 0
        
        else: result = 0
        
    else:
        
        user_confirmation = input(' You want to exit? Enter [YES], all other selections will return you to the menu.\n\t>>> ')
        if user_confirmation.upper() == confirmation or user_confirmation.upper() == confirmation[0:1:1] or user_confirmation.upper() == confirmation[0:2:1]:
            result = exit_clause
            print('\x1B[3m' + ' Exiting the Homework 5 Menu' + '\x1B[0m')   
        
        else: result = 0

    return result