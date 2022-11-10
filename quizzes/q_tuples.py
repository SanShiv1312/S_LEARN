import streamlit as st

st.subheader("`QUIZ ON TUPLES IN PYTHON`")

qs = st.radio("Which of the following is a Python tuple?",("Select an option", "[1, 2, 3]", "(1, 2, 3)", "{1, 2, 3}"))
if qs == "(1, 2, 3)":
    st.success("correct answer")
elif qs == "{1, 2, 3}":
    st.error("try again")
elif qs == "[1, 2, 3]":
    st.error("try again")
else :
    st.info("choose the correct option")


st.write(
    """

    ```
    >>>t=(1,2,4,3)
    >>>t[1:3]
    ```
    """
) 
qs = st.radio("What is the output of the above Python code? ",("Select an option", "(1,2)", "(1,2,4)", "(2,4)"))
if qs == "(2,4)":
    st.success("correct answer")
elif qs == "(1,2,4)":
    st.error("try again")
elif qs == "(1,2)":
    st.error("try again")
else :
    st.info("choose the correct option")



qs = st.radio("A Python tuple can also be created without using parentheses",("Select an option", "True", "False"))
if qs == "True":
    st.success("correct answer")
elif qs == "False":
    st.error("try again")
else :
    st.info("choose the correct option")



st.write(
    """

    ```
    aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
    ```
    """
) 
qs = st.radio("Choose the correct way to access value 20 from the following tuple ",("Select an option", "aTuple[1][1]", "aTuple[1:2](1)", "aTuple[1:2][1]"))

if qs == "aTuple[1][1]":
    st.success("correct answer")
elif qs == "aTuple[1:2](1)":
    st.error("try again")
elif qs == "aTuple[1:2][1]":
    st.error("try again")
else :
    st.info("choose the correct option")

