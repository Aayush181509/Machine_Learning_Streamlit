import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict

st.title('Classifying Iris Flowers')
st.markdown("Toy model to play to classify iris flowers into \
    (setosa,versicolor,virginica) based on their sepal/petal \
        and length/width.")

st.header("Plant Features")
col1,col2=st.columns(2)