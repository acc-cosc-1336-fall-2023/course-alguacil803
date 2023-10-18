import question_d
print("We will determine the day of the week, from the numbers 1-7.")
while True:
    while True:
        try:
            day = int(input("Enter a Number from 1-7: "))
            break
        except ValueError:
            print("NOT a whole number!")
    z = question_d.get_day_of_week(day)
    print(z)
    while True:
        y = input("Would you like to Try Again? y/n: ")
        if y == 'y' or y == "Y" or y =='yes' or y=='YES':
            break
        elif y == 'n' or y == 'N' or y =='no' or y=='NO':
            print("Exiting")
            break
        else:
            print("Invalid, Select Y or N")
    if y == 'n' or y == 'N' or y =='NO' or y=='no':
        break
        