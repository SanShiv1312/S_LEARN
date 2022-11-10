import streamlit as st 

st.subheader("`QUIZ ON SETS IN PYTHON`")

qs = st.radio("Which of these about a set is not true?",("Select an option", "Allows duplicate values", "Immutable data type", "Data type with unordered values"))
if qs == "Immutable data type":
    st.success("correct answer")
elif qs == "Allows duplicate values":
    st.error("try again")
elif qs == "Data type with unordered values":
    st.error("try again")
else :
    st.info("choose the correct option")


st.write(
    """
    ```
    >>> a={5,4}
    >>> b={1,2,4,5}
    >>> a<b
    ```
    """
)

qs = st.radio("What is the output of the above Python code? ",("Select an option", "{1,2}", "True", "False", "Invalid operation"))
if qs == "True":
    st.success("correct answer")
elif qs == "{1,2}":
    st.error("try again")
elif qs == "False":
    st.error("try again")
elif qs == "Invalid operation":
    st.error("try again")
else :
    st.info("choose the correct option")



qs = st.radio("Which of the following statements is used to create an empty set?",("Select an option", "{}", "[]", "()", "set()"))
if qs == "set()":
    st.success("correct answer")
elif qs == "{}":
    st.error("try again")
elif qs == "[]":
    st.error("try again")
elif qs == "()":
    st.error("try again")
else :
    st.info("choose the correct option")


