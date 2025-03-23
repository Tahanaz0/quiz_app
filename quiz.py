import streamlit as st
import random as rd

# Set page title and icon
st.set_page_config(page_title="Python Quiz", page_icon="🐍")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stRadio > div {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 10px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .feedback {
        font-size: 20px;
        font-weight: bold;
        padding: 10px;
        border-radius: 5px;
        margin-top: 20px;
    }
    .correct {
        color: #4CAF50;
    }
    .incorrect {
        color: #FF0000;
    }
    .motivation {
        font-size: 18px;
        font-style: italic;
        color: #555555;
        margin-top: 10px;
    }
    .heading {
        font-size: 36px;
        font-weight: bold;
        color: #2E86C1;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App heading
st.markdown("<div class='heading'>🐍 Python Quiz</div>", unsafe_allow_html=True)

# Motivational line
st.markdown("<div class='motivation'>Keep learning, keep growing! 🚀</div>", unsafe_allow_html=True)

# List of questions
questions = [
    {
        "question": "What is the purpose of the `range()` function in Python?",
        "options": ["A. To create a list", "B. To generate a sequence of numbers", "C. To split a string", "D. None of the above"],
        "answer": "B"
    },
    {
        "question": "What does the `len()` function do in Python?",
        "options": ["A. Checks the length of a string", "B. Multiplies numbers", "C. Sorts a list", "D. None of the above"],
        "answer": "A"
    },
    {
        "question": "What is the use of the `if-else` statement in Python?",
        "options": ["A. To run loops", "B. To check conditions", "C. To store data", "D. None of the above"],
        "answer": "B"
    },
    {
        "question": "Why is the `for` loop used in Python?",
        "options": ["A. To repeat a block of code", "B. To check conditions", "C. To encrypt data", "D. None of the above"],
        "answer": "A"
    },
    {
        "question": "What is a `dictionary` used for in Python?",
        "options": ["A. To store key-value pairs", "B. To sort numbers", "C. To create graphics", "D. None of the above"],
        "answer": "A"
    },
      {
        "question": "What is the output of `2 ** 3` in Python?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 10"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "What does the `append()` method do in Python?",
        "options": ["A. Adds an element to the end of a list", "B. Removes an element from a list", "C. Sorts a list", "D. Reverses a list"],
        "answer": "A"
    },
    {
        "question": "What is the correct way to create a comment in Python?",
        "options": ["A. // This is a comment", "B. /* This is a comment */", "C. # This is a comment", "D. <!-- This is a comment -->"],
        "answer": "C"
    },
    {
        "question": "What is the purpose of the `return` statement in a function?",
        "options": ["A. To stop the function", "B. To return a value from the function", "C. To print a value", "D. To define a variable"],
        "answer": "B"
    },
    {
        "question": "Which operator is used for floor division in Python?",
        "options": ["A. /", "B. //", "C. %", "D. **"],
        "answer": "B"
    },
    {
        "question": "What is the output of `'Hello' + 'World'` in Python?",
        "options": ["A. HelloWorld", "B. Hello World", "C. Hello+World", "D. Error"],
        "answer": "A"
    },
    {
        "question": "What does the `strip()` method do in Python?",
        "options": ["A. Splits a string", "B. Removes leading and trailing whitespace", "C. Converts a string to uppercase", "D. Reverses a string"],
        "answer": "B"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["A. List", "B. Dictionary", "C. Tuple", "D. Set"],
        "answer": "C"
    },
    {
        "question": "What is the purpose of the `import` statement in Python?",
        "options": ["A. To include external libraries", "B. To define a function", "C. To create a loop", "D. To print output"],
        "answer": "A"
    }
]

# Initialize session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = rd.choice(questions)
if 'show_feedback' not in st.session_state:
    st.session_state.show_feedback = False
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'total_questions' not in st.session_state:
    st.session_state.total_questions = 0

# Check if the quiz is complete
quiz_complete = st.session_state.total_questions >= len(questions)

# Display the current question or completion message
if not quiz_complete:
    # Display the current question
    question = st.session_state.current_question

    # Progress bar
    progress_value = st.session_state.total_questions / len(questions)
    st.progress(progress_value)

    # Display question
    st.markdown(f"### {question['question']}", unsafe_allow_html=True)

    # Display options
    select_option = st.radio("Select an option", question['options'], key='answer')

    # Submit button
    if st.button('Submit') and not st.session_state.show_feedback:
        # Extract the first character (A, B, C, D) from the selected option
        selected_answer = select_option[0]

        # Compare the selected answer with the correct answer
        if selected_answer == question['answer']:
            st.session_state.score += 1
            feedback = f"<div class='feedback correct'>✅ Correct! Well done!</div>"
        else:
            feedback = f"<div class='feedback incorrect'>❌ Incorrect! The correct answer is {question['answer']}.</div>"

        st.markdown(feedback, unsafe_allow_html=True)
        st.session_state.show_feedback = True
        st.session_state.total_questions += 1

    # Next Question button
    if st.session_state.show_feedback:
        if st.button('Next Question'):
            if st.session_state.total_questions < len(questions):  # Check if all questions are answered
                st.session_state.current_question = rd.choice(questions)
                st.session_state.show_feedback = False
                st.rerun()
else:
    # Quiz completion message
    st.markdown("<div class='feedback'>🎉 You've completed the quiz! 🎉</div>", unsafe_allow_html=True)
    st.markdown(f"### Final Score: {st.session_state.score}/{st.session_state.total_questions}", unsafe_allow_html=True)

# Display score
# st.markdown(f"### Score: {st.session_state.score}/{st.session_state.total_questions}", unsafe_allow_html=True)