from strings import get_dna_complement, get_hamming_distance
#lets try this 

def display_menu():
    print(" A- Hamming Distance")
    print("B - DNA Reverse Complement")
    print("C - Exit")

def run_menu():
    display_menu()
    option = str(input("select option A,B, or C:"))
    while (option != 'A'and option != 'B' and option != 'C'):
        option = str(input("option FAIL. select A,B,or C:"))
    select_option(option)

def select_option(option):
    if option =='A':
        option_A()
    if option == 'B':
        option_B()
    if option == 'C':
        option_C()

def option_A():
    print("\nyou selected option A, Enter B strings of equal length to find the hamming Distance ")
    y = hamming_parameter ()
    while y== "Invalid, both strings are not of equal length":
        print("These B strings aren't of equal length,try again.")
        y = hamming_parameter()
    print(f"\nTheHamming Distance between these two strings is {y}.\n")
    try_agin_option_A()

def option_B():
    print("\nYou selected option B, Enter a valid DNA strand to find the reverse complement")
    DNA_STRAND = str(input("Enter your DNA strand: "))
    y= get_dna_complement(DNA_STRAND)
    while y == "This sequence is not a DNA strand.":
        print("This strand is NOT a valid DNA strand")
        DNA_STRAND = str(input("Please Enter a Valid DNA strand: "))
        y= get_dna_complement(DNA_STRAND) 
    print (y)


def option_C():
    while True:
        exit = input("Are you sure you want to exit y/n: ")
        if exit == "yes" or exit == "y" or exit == 'Y' or exit == 'YES' :
            print("\nExiting program\n")
            break
        elif exit == "no" or exit == "n" or exit == 'N' or exit == 'NO' :
            run_menu
            break
        else:
            print("please enter yes or no")

def hamming_parameter():
    dna1 = str(input("Enter your 1st String: "))
    dna2 = str(input("Enter your 2nd string: "))
    y= get_hamming_distance(dna1, dna2)
    return y 

def try_agin_option_A():
    while True:
        x= str(input("press 'y if would like to try again, press 'n to return to main menu, press C to exit:"))
        if x == "yes" or x == 'Y' or x == 'YES':
            option_A()
            break
        if x == "no" or x == "n" or x == 'N' or x == 'NO':
            print("Returning to Main Menu\n")
            run_menu()
            break 
        if x== "C":
            option_C()
            break
        else:
            print("please enter 'y' or 'n' or 'C' ")

def try_agin_option_B():
    while True:
        x= str(input("press 'y' if would like to try again, press 'n' to return to main menu, press C to exit: "))
        if x == "no" or x== "n" or x == 'N' or x == 'NO':
            print ("Returning to main menu\n")
            run_menu()
            break
        if x == "C":
            option_C()
            break
        else:
            print("please enter 'y' or 'n' or 'C' ")

run_menu()