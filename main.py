import streamlit as st

st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQiX7NRuPjDQ7-Mb70rlGzlAUU_vF7w3E2tNw&s", use_container_width=True)

st.markdown("""<h1 style='text-align: center; font-size: 50px;'>Meta Scifor Mega Hiring</h1>""",
            unsafe_allow_html=True)

is_fresher = st.radio("Are you a fresher?", ("Yes", "No"))

if is_fresher == "Yes":
    st.write("Answer the below question correctly to get selected!")

    answer = st.slider("What is the decimal number equivalent to 101010?", min_value=1, max_value=100, value=50)
    correct_answer = 42

    if st.button("Submit Answer"):
        if answer == correct_answer:
            st.success("Congratulations! You are selected!")
        else:
            st.error("Sorry, wrong answer. Try again!")

