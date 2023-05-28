import streamlit as st
from pages.page2 import cal

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

y=cal(10)
y