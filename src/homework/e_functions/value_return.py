#
week_divisor = 60*60*24*7      #seconds
day_divisor = 60*60*24         #seconds
hour_divisor = 60*60           #seconds
minute_divisor = 60            #seconds

#def get_weeks(epoch_seconds):
#    return int(epoch_seconds//week_divisor)

#def get_days(epoch_seconds):
#    whole_weeks_rem = (epoch_seconds%week_divisor)
#    return int(whole_weeks_rem//day_divisor)

def get_hours(epoch_seconds):
    whole_days_rem = (epoch_seconds%week_divisor)%day_divisor
    return int(whole_days_rem//hour_divisor)

def get_minutes(epoch_seconds):
    whole_hours_rem = ((epoch_seconds%week_divisor)%day_divisor)%hour_divisor
    return int(whole_hours_rem//minute_divisor)

def get_seconds(epoch_seconds):
    whole_minutes_rem = (((epoch_seconds%week_divisor)%day_divisor)%hour_divisor)%minute_divisor
    return int(whole_minutes_rem)

def current_time_only(epoch_seconds):

    whole_days_rem = (epoch_seconds%week_divisor)%day_divisor
    whole_hours_rem = whole_days_rem%hour_divisor
    whole_minutes_rem = whole_hours_rem%minute_divisor
    am_pm = 'AM'

    if int(whole_days_rem//hour_divisor) >= 13: 
        hours = str(int(whole_days_rem//hour_divisor) - 12) 
        am_pm = 'PM'
    else: hours = str(int(whole_days_rem//hour_divisor))

    if hours == '0': hours = '12'

    if len(hours)<2: hours = '0' + hours

    minutes = str(int(whole_hours_rem//minute_divisor))

    if len(minutes)<2: minutes = '0' + minutes

    seconds = str(int(whole_minutes_rem))

    if len(seconds)<2: seconds = '0' + seconds

    print('The current time is: ' + hours + ':' + minutes + ':' + seconds + ' ' + am_pm)