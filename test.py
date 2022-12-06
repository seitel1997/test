#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


st.title('BONJORNO')

df=pd.read_csv('Bastar Craton.csv')
df

data=df.loc[3:9,['MGO(WT%)','SIO2(WT%)']]
plt.scatter(data['MGO(WT%)'],data['SIO2(WT%)'])
