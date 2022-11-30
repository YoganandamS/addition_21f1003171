import streamlit as st

st.header('Addition_y')


def add():
    num1 = st.number_input("Enter a number")
    num2 = st.number_input("Enter another number")
   
    return (num1+num2)

Sum = add()
   
st.write(Sum) 
