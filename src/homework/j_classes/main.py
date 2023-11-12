import class_a
user_input = str(input("Press Y to roll: ")).lower()
while user_input == 'y':
     dice = class_a.Die()
     dice.roll()
     print("You rolled a ", dice.get_role_value())
     print(dice)
     user_input = str(input("Press Y to try again: ")).lower()
     print(" ")