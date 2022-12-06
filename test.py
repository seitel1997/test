#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title('BONJORNO')

sel1=st.selctbox('Selection', [1,2,3])
st.write('Deine Auswahl ist: ', sel1)

x=np.linspace(0,50,50)
plt.plot(x, X**2)

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
