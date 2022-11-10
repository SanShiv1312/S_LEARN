from email.policy import default
from turtle import color
import streamlit as st 
from streamlit_option_menu import option_menu 
import streamlit_book as stb


with st.sidebar:
    selected = option_menu(
        menu_title="S-LEARN",
        options = ['Home', 'My Learning', 'Quiz', 'Feedback'], ##sub-headers 
        icons=['house', 'journals', 'pencil-square', 'chat-square-text'], ##icons imported from bootstrap
        styles={
            "nav-link-selected": {"background": " #40a48e", "color": "black"}
        }
    )

if selected == "Home":
    st.title("welcome to `S-LEARN`🎓🌟")
    st.subheader(" This web app is an E-Learning Platform which includes basics of *`Data Structures`*, which are crucial in programming.")
    st.markdown("### `Contents of this web app : `")
    st.write(
                    """    
            -	#### `My Learning`
            The key concepts of Basic Data Structures in Python will be available over here, which are ready to refer.. 

            -   #### `Quiz`
            Place where you can test your learning(Concept-Specific)

            -   #### `Feedback`
            You can drop your valuable suggestions and thoughts.. 
                    """
                )


if selected == "My Learning":
        
        stb.set_book_config(menu_title="Chapters",
                menu_icon="lightbulb", 
                options=[
                    "Introduction",
                    "Lists in Python",
                    "Tuples in Python",
                    "Dictionaries in Python",
                    "Sets in Python",
                    ],
                styles={
                    "nav-link-selected": {"background": "aqua", "color": "black"}
                },
                icons=[
                    "code",
                    "code",
                    "code",
                    "code",
                    "code",
                    ],
                paths=[
                    "st_files/Introduction.py",
                    "st_files/lists_in_py.md",
                    "st_files/tuples_in_py.md",
                    "st_files/dictionaries_in_py.md",
                    "st_files/sets_in_py.md",
                    ]
            )
if selected == "Quiz":
    stb.set_book_config(menu_title="Quiz",
                menu_icon="controller", 
                options=[
                    "Quiz on Lists",
                    "Quiz on Tuples",
                    "Quiz on Dictionary",
                    "Quiz on Sets",
                    ],
                icons=[
                    "pencil-square",
                    "pencil-square",
                    "pencil-square",
                    "pencil-square",
                    ],
                paths=[
                    "quizzes/q_lists.py",
                    "quizzes/q_tuples.py",
                    "quizzes/q_dictionaries.py",
                    "quizzes/q_sets.py",
                    ]
            )

with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

if selected == "Feedback":
    with st.form(key='my_form'):
        text_input = st.text_input(label='Enter your name')
        submit_button = st.form_submit_button(label='')

    form = st.form(key='my-form')
    name = form.text_input('Give your Feedback')
    submit = form.form_submit_button('')
    if st.button("Submit feedback"):
        st.success("Thanks for your feedback 🌷")
