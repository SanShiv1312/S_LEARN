import streamlit as st

st.subheader("`QUIZ ON DICTIONARIES IN PYTHON`")

qs = st.radio("Which of the following statements create a dictionary?",("Select an option", "d = {}", "d = {“john” : 40, “peter” : 45}", "d = {40 : ”john”, 45 : ”peter”}", "All the mentioned"))
if qs == "All the mentioned":
    st.success("correct answer")
elif qs == "d = {}":
    st.error("try again")
elif qs == "d = {“john” : 40, “peter” : 45}":
    st.error("try again")
elif qs == "d = {40 : ”john”, 45 : ”peter”}":
    st.error("try again")
else :
    st.info("choose the correct option")

st.write(
    """
    ```
    d = {"john":40, "peter":45}
    "john" in d
    ```
    """
)
qs = st.radio("What will the output for the above code snippet?",("Select an option", "Error", "True", "False"))
if qs == "True":
    st.success("correct answer")
elif qs == "False":
    st.error("try again")
elif qs == "Error":
    st.error("try again")
else :
    st.info("choose the correct option")


qs = st.radio("Items are accessed by their position in a dictionary and All the keys in a dictionary must be of the same type.",("Select an option", "True", "False"))
if qs == "False":
    st.success("correct answer")
elif qs == "True":
    st.error("try again")
else :
    st.info("choose the correct option")