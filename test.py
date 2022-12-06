#!/usr/bin/env python
# coding: utf-8

# In[ ]:


option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

