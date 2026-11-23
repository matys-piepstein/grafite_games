import streamlit as st


def pedir_numero(mensaje):
    while True:
        try:
            return float(st.numbrer_input(mensaje))
        except ValueError:
            print("Error: Debes introducir un número válido, no letras.\n")

def introduccion():
    while True:
        num1 = pedir_numero("Introduce el primer número: ")
        op = st.text_input("Introduce la operación (+, -, *, /): ")
        num2 = pedir_numero("Introduce el segundo número: ")
        
        if op in ["+", "-", "*", "/"]:
            return num1, op, num2
        else:
            print("No es una operación válida. Introduce +, -, * o /\n")

def calculo(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "Error: No se puede dividir entre cero"
        return num1 / num2

num1, op, num2 = introduccion()
res = calculo(num1, op, num2)
st.write("Resultado:", res)
