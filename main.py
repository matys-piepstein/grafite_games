import streamlit as st
import random

st.title("Bienvenidos a grafite games")

parte = st.radio(
    "donde jugar",
    ["descargar","online"]
)

if parte == "online" :
    if st.buton("calculadora"):
        st.swich_page("calculator.py")


