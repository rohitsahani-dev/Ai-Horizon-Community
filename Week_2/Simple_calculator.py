import streamlit as st

st.title("Simple Calculator")

st.write("Enter two number ans select an operation : ")

num1 = st.number_input("Enter first number : ",value=0.00)
num2 = st.number_input("Enter second number : ",value=0.00)

operation = st.selectbox("Operation",("Add", "Subtract", "Multiply", "Divide", "Exponent", "Modulo"))

result = None

if st.button("Calculate"):
   try:
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Division by zero is not allowed.")
        elif operation == "Exponent":
            result = num1 ** num2
        elif operation == "Modulo":
            result = num1 % num2

        if result is not None:
            st.success(f"Result: {result}")

   except Exception as e:
        st.error(f"Error: {e}")


st.info("Update numbers or operation and click Calculate.")