import numpy as np
import pandas as pd
import streamlit as st
import os
from PIL import Image
from pathlib import Path


def getPathInStreamlitDir():
    return Path(__file__).parents[1] / str('streamlit/')


st.title('This is a test of Streamlit cloud from Deepnote through Github')

st.text("This is a local image.")

img_name = 'test-pattern.png'
img_path = getPathInStreamlitDir() / str('assets/' + img_name)
image = Image.open(img_path)
st.image(image)

st.text('This is a dataframe from a csv file.')

df = pd.read_csv(getPathInStreamlitDir() / str('data/IRIS.csv'))

st.dataframe(df)

'''
This was the key to be able to get to files with the same line of code in Deepnote and Streamlit

print(Path(__file__).parents)
print(Path(__file__).parents[0])
print(Path(__file__).parents[1])
print(Path(__file__).parents[2])
print(Path(__file__).parents[3])

<PosixPath.parents>
/work/Streamlit_demo/For_github/streamlit
/work/Streamlit_demo/For_github
/work/Streamlit_demo
/work
'''