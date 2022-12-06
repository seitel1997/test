#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title('BONJORNO')

option = st.selectbox(
    'wie geht´s?',
    ('gut', 'mäh', 'schlecht'))

