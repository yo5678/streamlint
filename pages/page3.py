import streamlit as st

st.markdown("# page3 🎈")
st.sidebar.markdown("# page3 🎈")

import streamlit as st
import pandas as pd


test=True

if test:
    st.write("Here's our first attempt at using data to create a table:")
    st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }))

