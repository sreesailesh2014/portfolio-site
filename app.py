import streamlit as st

# Title
st.title("Hello GitHub + Streamlit")

# Input field
name = st.text_input("Enter your name:")

# Button
if st.button("Greet Me"):
    st.success(f"Hello {name}, welcome to Streamlit!")

# Display info
st.write("This is a simple demo app you can push to GitHub.")
