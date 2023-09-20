import decisions

options = int(input('what was your score?'))
total = int(input('what was the total possible?'))

rating = decisions.get_faculty_rating(decisions.get_options_ratio(options,total))

print('Your Score ' + str(round(decisions.get_options_ratio(options,total)*100)) + ', ' + rating)
