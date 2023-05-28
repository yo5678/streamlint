import streamlit as st
from pages.How_to_calculate import get_timezone,get_newtime

st.title("What time is there!")
st.sidebar.markdown("# What time is there!")


options = st.selectbox(
    'select place where you want to know time now',
    ['SiliconValley', 'Hollywood',"USOpen"])

st.write('You selected:', options)


get_timezone=get_timezone(options)
new_time=get_newtime(get_timezone)

st.write(f' {options} time is: ', new_time)
