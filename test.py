#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title('BONJORNO')

sell=st.selctbox('Selection', [1,2,3])


arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
