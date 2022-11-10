import streamlit as st 
from PIL import Image

st.header('Data Structures in `Python`')
st.markdown(' ##### Data Structures in any programming language are the key to write or build an efficient code. More Precisely Python has edge over other programming languages in terms of more understandability of Data Structures concepts and the utility. Data Structures are a way of organizing data so that it can be accessed more efficiently according to the context. ')

col1, col2, col3 = st.columns([1,6,1])

with col1:
  st.write("")

with col2:
  st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStjlbVkV4wUhAOQZFLZKwMme2jPzfL64MZaA&usqp=CAU.png", width=550)

with col3:
  st.write("")

st.write("In this context we will have some brief glimpse of each in-built data structure in Python and how they are related to some specific Python Data Type")
st.markdown("More precisely we will have the discussion and descripton about basic in-built data structures namely :")

st.write(
                    """    
            -	### `List`
            -	### `Tuples`
            -	### `Dictionaries`
            - ### `Set`
                    """
                )

