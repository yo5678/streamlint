import streamlit as st


import streamlit as st
import numpy as np
import pandas as pd


def cal(x):
    y=x**2
    return y

test=False

if test:

   st.markdown("# page2 🎈")
   st.sidebar.markdown("# page2 🎈")
   if st.checkbox('Show dataframe'):
      chart_data = pd.DataFrame(
         np.random.randn(20, 3),
         columns=['a', 'b', 'c'])

      chart_data