#arithmetic operators
# x = 6
# y = 3
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x**y)
# print(x//y)
# print(x%y)

#assignment operators

# a = 10
# b = 11
# b -= a
# print(a)
# print(b)


# a = 10
# b = 11
# b *= a
# print(a)
# print(b)

# a = 10
# b = 11
# b /= a
# print(a)
# print(b)

# a = 10
# b = 11
# b //= a
# print(a)
# print(b)

# a = 10
# b = 11
# b **= a
# print(a)
# print(b)

#comparison operator

# a = 10
# b = 10
# print(a == b)

# a = 10
# b = 11
# print(a != b)

# a = 10
# b = 11
# print(a < b)

# a = 10
# b = 11
# print(a > b)

#logical operators
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# print(not True)
# print(not False)

# x = 5
# print( x< 3 and x < 10)
# print( x< 3 or x < 10)
# print( not(x>3 and x<10))

#identity operators

# x = int("1000")
# y = int("1000")
# print (x == y)
# print (x is y) # to compare the memory space
# print(id(x), id(y)) 

# x = 10000
# y = 10000
# print(id(x), id(y)) 
# print (x == y)
# print (x is y) # to compare the memory space

# x = 1000
# y = 1000
# print(id(x), id(y))   # Shows memory addresses
# print(x is y)         # Identity check

# x = ["apple","banana"]
# y = ["apple","banana"]
# z = x

# print (x == y)
# print (y == z)
# print (x == z)
# print (x is y)
# print (x is z)
# print (y is z)
# print(id(x), id(y), id(z))

x = ["apple","banana"]
y = ["APPLE","banana"]
z = x

# print (x == y)
# print (y == z)
# print (x == z)
# print (x is y)
# print (x is z)
# print (y is z)
# print (x is not y)
# print (x is not z)
# print (x!=y)
# print (x!= z)
# print(id(x), id(y), id(z))

#membership operator
# x = ["apple","banana"]
# print("banana"in x)
# print("banna"in x)
# print("pineapple"not in x)

# text = "Hello World"
# print(id(text))
# print("H"in text)
# print("Hello" in text)
# print("z" not in text)

#operator precedence
# print ()- (6+3))
# print(100+5*3)
# print(5 +4 -7+3) #left to right
# print(100 - 3**5)
# print(5 == 4+1)
# print(not(5 == 5))
# print(1 or 2 and 3) #to be discussed later
# print(4 or 5)# to be discussed later(6+3

# import streamlit as st
# import pandas as pd
# import numpy as np

# # Title and header
# st.title("My First Streamlit App")
# st.header("Practice Dashboard")

# # Text input
# name = st.text_input("Enter your name:")
# if name:
#     st.write(f"Hello, {name}! 👋")

# # Button interaction
# if st.button("Click me"):
#     st.success("You clicked the button!")

# # Slider
# number = st.slider("Pick a number", 1, 100, 25)
# st.write("Your number squared is:", number ** 2)

# # Random data chart
# data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['A', 'B', 'C']
# )
# st.line_chart(data)

streamlit run d:/python_classes/class_1/operators.py



