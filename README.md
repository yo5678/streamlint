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



## making app

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


### Tips
python command collection:

https://qiita.com/HyunwookPark/items/242a8ceea656416b6da8