#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


st.title('BONJORNO')

df=pd.read_csv('Bastar Craton.csv')

el1 ='MnO'
el2 = 'SiO2'
plt.scatter(dfM[el1],df[el2], label='MinData')
plt.xlabel(el1)
plt.ylabel(el2)
plt.legend(loc='lower right')
plt.show()
