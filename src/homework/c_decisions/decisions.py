def get_options_ratio(option, total):
    result = option / total
    return result

def get_faculty_rating(score):
    ratio = score
    unacceptable = .6
    needs_improvement = .7
    good = .8
    very_good = .9
    excellent = 1
    
    if ratio < unacceptable: result = 'is Unacceptable...'
    elif ratio < needs_improvement: result = 'Needs Improvement'
    elif ratio < good: result =  'is Good'
    elif ratio < very_good: result =  'is Very Good'
    elif ratio <= excellent: result = 'is Excellent!'
    elif ratio > 1: result = 'is impossible.'
    
    return result