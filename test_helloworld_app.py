import streamlit as st

def hello_world():
    print("Hello, World!")

st.title("Hello World Streamlit App")

st.write("Click the button below to print 'Hello, World!' in the console.")

if st.button("Click me!"):
    hello_world()