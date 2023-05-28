import inspect
import os
from tzlocal import get_localzone

def get_local_timezone():
    local_timezone = get_localzone()
    return local_timezone

get_cal_code=inspect.getsource(get_local_timezone)

print(get_cal_code)

print(type(get_cal_code))