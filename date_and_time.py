import time as timemodule  # clashes with datetime.time
from datetime import date 
from datetime import time
from datetime import datetime

epoch_seconds = 1602858597    # Friday, October 16, 2020 2:29:57 PM GMT

time_struct = timemodule.localtime(epoch_seconds)
print(type(time_struct), time_struct)   # <class 'time.struct_time'> time.struct_time(tm_year=2020, tm_mon=10, tm_mday=16, tm_hour=19, tm_min=59, tm_sec=57, tm_wday=4, tm_yday=290, tm_isdst=0)

date = date(*time_struct[:3])
print(date)
time = time(*time_struct[3:6])
print(time)
timestamp = datetime(*time_struct[:6])
print(timestamp)
