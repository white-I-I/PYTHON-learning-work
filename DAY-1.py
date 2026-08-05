

#---------My First python code-----------------------------------------------
print("This is my First python program i printed. \n I started python from today (3-8-2026).\n\n") 

#--Variables-----------------------------------------------------------------
#--(stores information). 
# real-Example
#Your bag contains:
#📚 Books
#✏️ Pens
#The bag is the container.
#Similarly, a variable is a container that holds data.

#--[Name Box → user]
#--[Age Box → 19]
#--[City Box → New Tork] 

name = "one"
print(name) 

#--Data Types-----------------------------------------------------------------
#--Integer (int)-Whole numbers

age = 20
age1 = 100
print(age, age1) 

#--Float (float)-Decimal numbers
height = 6.9
print(height)

#--String (str)-Text or words 
name = "black"
print(name) 

#--Boolean (bool)-Only two values. (TRUE AND FALSE).
#--Used for yes/no situations. 
student_user = True
print(student_user)
print(type(student_user))

#--input()---------------------------------------------------------------------
#--give input to python. or Python asks the user.
name = input("Enter your python name:")
print("Hello", name) 

#--type() Function-------------------------------------------------------------
#--The type() function tells you what type of data a value is. 
age = 10.1
print(type(age)) 

#--Type Casting----------------------------------------------------------------
#--Type casting means changing one data type into another.
#Text ➜ Number and reverse
#Integer ➜ Float and reverse

age = 10
print(type(age))

b= float(age)
print(b)
print(type(b))



