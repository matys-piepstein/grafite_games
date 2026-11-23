import streamlit as st
import random

st.title("Bienvenidos a grafite games")

parte = st.radio(
    "donde jugar",
    ["descargar","online"]
)

if parte == "online" :
    if st.button("calculadora"):
        st.switch_page("calculator.py")


