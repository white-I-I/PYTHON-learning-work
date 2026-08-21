

#---------My First python code-----------------------------------------------
print("HELLO WORLD")
print("This is my First python program i printed. \n I started python from today (3-8-2026).\n\n")
 
print("sai\n" * 10) 

#--Variables-----------------------------------------------------------------
"""--(stores information). 
real-Example
Your bag contains:
📚 Books
✏️ Pens
The bag is the container.
Similarly, a variable is a container that holds data."""

#--[Name Box → user]
#--[Age Box → 19]
#--[City Box → New Tork] 

name = "one"
print(name) #Output: one

#--Data Types-----------------------------------------------------------------
#--Integer (int)-Whole numbers

age = 25
age1 = 100
print(age, age1) #Output: 25 100

#--Float (float)-Decimal numbers
height = 6.9
print(height) #Output: 6.9

#--String (str)-Text or words 
name = "black"
print(name) #Output: black

#--Boolean (bool)-Only two values. (TRUE AND FALSE).
#--Used for yes/no situations. 
age = 25
a = age > 18
print(a)  #Output: True
b = age < 10
print(b)  #Output: False 

#--input()---------------------------------------------------------------------
"""give input to python. or Python asks the user."""
name = input("Enter your python name:")
print("Hello", name) #Output: user input

#--type() Function-------------------------------------------------------------
"""The type() function tells you what type of data a value is."""
age = 10.1
print(type(age)) #Output: <class 'float'>

#--Type Casting----------------------------------------------------------------
"""Type casting means changing one data type into another.
Text ➜ Number and reverse
Integer ➜ Float and reverse"""

age = 10
print(type(age)) #Output: <class 'int'>

b= float(age) 
print(b)  #Output: 10.0
print(type(b)) #Output: <class 'float'> 

#------------------------------------------------------------------------------------------------

"""
\n → New Line
Moves the text to the next line.

\t → Tab (Big Space)
Adds a tab space.

\n\n → Blank Line
Leave one empty line.

\" → Double Quotes.
Print double quotes inside text.

\' → Single Quote
Print a single quote inside text.

\\ → Backslash
Print a backslash.
"""

