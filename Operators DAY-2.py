#-----------------------------------------Operators--------------------------------------
"""Why Do We Need Operators?
Without operators, Python cannot calculate.
An operator is a symbol that tells Python to perform an operation. (what action to perform)"""
#--Arithmetic Operators---------------------------------------------
#--- (+, -,  *,  /,  //,  %,  **)
"""Arithmetic operators are simply math symbols that Python understands. """
 
a = 20
b = 10 
print(a+b) #output: 30
print(a-b) #output: 10
print(a*b) #output: 200 
print(a/b) #output: 2.0 (always returns a float (decimal number).
print(a//b) #output: 2  (quotient) (ignoring the decimal part.)
print(a % b) #output: 0  (remainder)
print(a ** b) #output: 102400..   (2 ** 3 = 2 x 2 x 2 = 8)

#----Arithmetic = calculations.

#--Assignment Operators ----------------------------------------------
#--- ( =)
"""Assignment operators are used to store or change values in variables."""
#-- (=)- "put this value into this variable." (= means assign)
#-example
age = 15
name = "Alex" 

# Assignment = store/update a value.


#--Comparison Operators (Relational Operators)--------------------------
#--- (==,  !=,  >,  <,  >=,  <=) 
"""Comparison operators compare two values. True or False.""" 
#--(==)-Equal (== means compare)
a=5
b=8
print(5 == 5) #output: TRUE
print(5 == 10) #output: FALSE 
print(a != b)   # True (!= not equal)
print(a > b)    # True
print(a < b)    # False
print(a >= b)   # True
print(a <= b)    # False 

# Relational = comparison.


#--Bitwise Operators-----------------------------------------------------
#--- (&,  |,  ^,  ~,  <<,  >>) (binary values - 0 and 1)
"""& →  AND
   | →  OR
   ^ →  XOR
   ~ → NOT
   << → Left shift
   >> → Right shift """
"""Bitwise operators work only with the binary. form of integers."""  
a = 5 #(101)
b = 3 #(011) 
print( a & b) 
print ( a | b)
print(a ^ b)
print(~a)
print(a << 1)

# Bitwise = works with binary bits.


#--Logical Operators------------------------------------------------------
#--- (and,  or,  not) 
"""Logical operators are used to combine conditions"""

a = 10

print (a>9 and a<11) #- Both conditions must be true. 
print (a > 20 or a<11) #- At least one condition must be true. 
print( not( a<9)) #-not reverses True/False.  

# Logical = combines conditions.


#-- Compound Operators----------------------------------------------------
#--- (+=, -=, *=, /=, //=, %=, **=, &=, `, ^=, >>=)
"""This is closely related to assignment operators.""" #(combine: operation + assignment) 
x = 10
x += 5
print(x) #OUTPUT: 15 (x = x + 10) 

#Compound = Operation + assignment


#-- Membership Operators--------------------------------------------------
#--- ( in,  not in)
"""They check whether a value exists inside a collection or sequence."""

fruit = ["orange", "mango", "banana", "watermillon"]
print("watermillon" in fruit) #('watermillon' is inside the list.) (TRUE)
print("apple" not in fruit) #('apple' is not in the list.) (TRUE)

print("apple" in fruit) #FALSE 

#Membership = check whether something is present.


#-- Identity Operators---------------------------------------------------
#--- (is,  is not) 
"""They check whether two variables refer to the same object,
    rather than simply having equal values."""

a = [1, 2, 3]
b = a
print(a is b) #TRUE
print(a is not b) #FALSE

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) #(Are they the exact same object?) #FALSE 

#Identity = check whether objects are the same.


