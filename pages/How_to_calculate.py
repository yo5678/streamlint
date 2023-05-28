import streamlit as st
import numpy as np
import pandas as pd
import inspect
from datetime import datetime
from pytz import timezone
from tzlocal import get_localzone



st.markdown("## How to calculate")
st.sidebar.markdown("# How to calculate")


st.markdown("At first, you have to get new timezone")
st.markdown("I want to make the processing more intelligent.")
def get_timezone(options):
    """_summary_:get timezone

    Args:
        options (str): place which is selected

    Returns:
        str: return timezone
    """
    if options=='SiliconValley' or 'Hollywood':
        return 'America/Los_Angeles'
    elif options=='USOpen':
        return 'America/New_York'
    else:
        return "Error"
    
st.code(inspect.getsource(get_timezone), language='python')


st.markdown("Next, you have to get time where you selected")
def get_newtime(get_timezone):
    """_summary_:get new time

    Args:
        timezone (str): timezone like 'America/New_York'which is returned by get_timezone function.

    Returns:
        str: return time which is timezone like 2023-05-27 22:47:55.957684-07:00
    """
    new_timezone = timezone(get_timezone)
    new_timezone_time = datetime.now(new_timezone)
    return new_timezone_time

st.code(inspect.getsource(get_newtime), language='python')