#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


st.title('BONJORNO')

df=pd.read_csv('Bastar Craton.csv')

sely=st.selectbox('Selection',['Sm/Nd','Rb/Sr'])

fig, ax = plt.subplots()


st.pyplot(fig)           
           
