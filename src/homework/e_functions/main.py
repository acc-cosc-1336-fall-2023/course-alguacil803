#
import time, value_return

epoch_seconds = time.time()
utc_to_cst = 5*60*60           
mid_week_epoch_start_correction = 3*60*60*24
test_hours_removal = 0*60*60
override_seconds = 3800

epoch_seconds -= utc_to_cst
epoch_seconds -= mid_week_epoch_start_correction
epoch_seconds -= test_hours_removal

if override_seconds != 0: epoch_seconds = override_seconds

#print(value_return.get_seconds(epoch_seconds))

#value_return.get_time(3800)
value_return.current_time_only(epoch_seconds)
