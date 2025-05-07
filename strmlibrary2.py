import streamlit as st

st.sidebar.title("Navigation")
# page = "Home"
page = st.sidebar.selectbox("Choose a screen",
                            ["Home",
                             "Addition",
                            "Subtraction"])
if st.sidebar.button("Home"):
    page = "Home"
if st.sidebar.button("Addition"):
    page = "Addition"

if page == "Home":
    st.title("Hello world")
    st.header("Welcome to my system")
    st.subheader("This is a subheader")
    st.write("This is a simple text")
    st.markdown("**Bold**, *italic* ")
    st.markdown("and [link](https://wis.edu.hn)")
    name = st.text_input("Enter your name")
    age = st.number_input("Enter yout age", min_value=0)
    if st.button("Greet"):
        st.success(f"Hello {name} and you have {age}")
        st.write(f"Hello {name} and you have {age}")

elif page == "Addition":
    st.title("Addition")
    number1 = st.number_input("Enter the first number")
    number2 = st.number_input("Enter the second number")
    if st.button("Sum"):
        st.write(f"The result is: {number1 + number2}")

elif page == "Subtraction":
    st.title("Subtraction")
    number1 = st.number_input("Enter the first number")
    number2 = st.number_input("Enter the second number")
    if st.button("Subtract"):
        st.write(f"The result is: {number1 - number2}")
