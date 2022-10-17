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

