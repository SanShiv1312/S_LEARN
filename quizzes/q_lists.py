import streamlit as st

st.subheader("`QUIZ ON LISTS IN PYTHON`")

qs = st.radio(" Suppose listx is [‘h’, ’e’, ’l’, ’l’, ’o’], what is len(listx)?",("Select an option", "4","5","Error"))
if qs == "5":
    st.success("correct answer")
elif qs == "4":
    st.error("try again")
elif qs == "Error":
    st.error("try again")
else :
    st.info("choose the correct option")


st.write(
    """

    ```
    sampleList = [10, 20, 30, 40, 50]
    sampleList.pop()
    print(sampleList)

    sampleList.pop(2)
    print(sampleList)
    ```
    """
) 
qs = st.radio("What is the output of the above list function? ",("Select an option", "[20, 30, 40, 50] & [10, 20, 40]", "[10, 20, 30, 40] & [10, 20, 30, 50]", "[10, 20, 30, 40] & [10, 20, 40]"))
if qs == "[10, 20, 30, 40] & [10, 20, 40]":
    st.success("correct answer")
elif qs == "[20, 30, 40, 50] & [10, 20, 40]":
    st.error("try again")
elif qs == "[10, 20, 30, 40] & [10, 20, 30, 50]":
    st.error("try again")
else :
    st.info("choose the correct option")



qs = st.radio("Suppose list1 is [2445, 133, 12454, 123], what is max(list1)? ",("Select an option", "2445", "12454", "133"))
if qs == "12454":
    st.success("correct answer")
elif qs == "133":
    st.error("try again")
elif qs == "2445":
    st.error("try again")
else :
    st.info("choose the correct option")



qs = st.radio("Suppose list_ab is [2, 33, 222, 14, 25], What is list_ab[-1]? ",("Select an option", "2", "14", "25"))
if qs == "25":
    st.success("correct answer")
elif qs == "14":
    st.error("try again")
elif qs == "2 ":
    st.error("try again")
else :
    st.info("choose the correct option")


st.write(
    """

    ```
    aList = [4, 8, 12, 16]
    aList[1:4] = [20, 24, 28]
    print(aList)
    ```
    """
) 
qs = st.radio("What is the output of the above code? ",("Select an option", "[4, 20, 24, 28, 8, 12, 16]", "[4, 20, 24, 28]", "Error"))
if qs == "[4, 20, 24, 28]":
    st.success("correct answer")
elif qs == "[4, 20, 24, 28, 8, 12, 16]":
    st.error("try again")
elif qs == "Error":
    st.error("try again")
else :
    st.info("choose the correct option")

    