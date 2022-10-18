import numpy as np
import pandas as pd
import streamlit as st
import os
from PIL import Image
from pathlib import Path
import altair as alt


def getPathInStreamlitDir():
    return Path(__file__).parents[1] / str('streamlit/')


st.title('This is a test of Streamlit cloud from Deepnote through Github')

img_name = 'test-pattern.png'
img_path = getPathInStreamlitDir() / str('assets/' + img_name)
image = Image.open(img_path)
st.image(image)


st.markdown('''This example was created to show how to reference file locations with the same line of code from both the Deepnote environment
and the Streamlit cloud. You can see the file structure in Github: 
[https://github.com/legolego/Streamlit_demo](https://github.com/legolego/Streamlit_demo)''')

st.markdown('''The test image above lives is in `streamlit/assets`.''')



st.markdown('The dataframe below is from a csv file that lives in `streamlit/data`.')

csv_path = getPathInStreamlitDir() / str('data/IRIS.csv')

df_iris = pd.read_csv(csv_path)

st.dataframe(df_iris)

st.markdown('''```from pathlib import Path``` was used to reference the file structure in both environments. 
This was the key to be able to get to files with the same line of code in Deepnote and Streamlit. Below are some examples, and notice
```Path(__file__).parents[1]``` ''')

st.code('''
print(Path(__file__).parents)
print(Path(__file__).parents[0])
print(Path(__file__).parents[1])  // <-- this line
print(Path(__file__).parents[2])
print(Path(__file__).parents[3])
''')

st.text('The code above results in:')
st.code('''
<PosixPath.parents>
/work/Streamlit_demo/For_github/streamlit
/work/Streamlit_demo/For_github    // <-- this result
/work/Streamlit_demo
/work
''')

st.markdown('A function was made to bring back the root of the path needed inside the `streamlit` folder.')

st.code('''
def getPathInStreamlitDir():
    return Path(__file__).parents[1] / str('streamlit/')
    ''')

st.markdown('The full paths for the image and csv are in the following variables:')

st.code('''
img_path = getPathInStreamlitDir() / str('assets/' + img_name)
csv_path = getPathInStreamlitDir() / str('data/IRIS.csv')
''')

st.text("Now let's make an Altair plot for fun.")

plot = alt.Chart(df_iris).mark_point().encode(
  # Map the sepalLength to x-axis
    x = 'sepalLength',
  # Map the petalLength to y-axis
    y = 'petalLength',
    color = 'variety'
)

st.altair_chart(plot)
