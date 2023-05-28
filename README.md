# streamlint
try_streamlint_firsttime


## Installation
I use Mac PC(already install Xcode command line).
I used below tools.

- python3.9.6
- venv


making virtual environment
~~~
python3 -m venv venv

. venv/bin/activate

pip install streamlit

streamlit hello
~~~


When I enter "streamlit hello", I faced error like below.
~~~
ImportError: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with LibreSSL 2.8.3. See: https://github.com/urllib3/urllib3/issues/2168
~~~

I do following command and work properly.
~~~
pip install -U pip
pip install urllib3==1.26.15
~~~



## learn how to use

~~~
touch my_script.py
~~~

edit my_script.py
~~~
"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
~~~

~~~
 streamlit run my_script.py
~~~

Here is any example:https://docs.streamlit.io/library/get-started/main-concepts

In this section, I tried mulitupy page.

I made directly like below.

~~~
page1.py
pages/
 |-page2.py
 |-page3.py
~~~


page1.py like below.

~~~
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
~~~

page2.py like below.

~~~
import streamlit as st

st.markdown("# page2 🎈")
st.sidebar.markdown("# page2 🎈")

import streamlit as st
import numpy as np
import pandas as pd


def cal(x):
    y=x**2
    return y

test=True

if test:
   if st.checkbox('Show dataframe'):
      chart_data = pd.DataFrame(
         np.random.randn(20, 3),
         columns=['a', 'b', 'c'])

      chart_data
~~~

page3.py like below.

~~~
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
~~~


I understand we can You can choose whether to display the page content（The table of contents is always displayed.）.


##  App





### Tips
python command collection:

https://qiita.com/HyunwookPark/items/242a8ceea656416b6da8

マークダウンからpythonコードを抜き出してsteramlintに突っ込むか？