#-----------------------------------Conditional Statements---------------------------
#---if 
"""Do something only if a condition is True.
   (or) To run code only when a condition is true"""

a = 20
if a >= 18:
    print("Entry allowed") #OUTPUT: Entry allowed
print(dir(a)) # showes all tags
print(type(a))

#----------------------------------------------------------------
#---else
"""To make Python execute code when a condition is False, you use the else statement.

    if condition:
    # if True
else:
    # if False"""

age = 20 

if age >= 18:
    print("You Can Enter") 
else:                          #output: You Can Enter
    print("You cant Enter")


#-------------------------------------------------------------------
#---elif
"""Otherwise, if this condition is true..."""

a = 41
if a == 20:
    print("A")
elif a >= 40:    #OUTPUT: B 
    print("B")
else:
    print("D")

#--------------------------------------------------------------------
#---and With if
"""and means both conditions must be True."""

a = 18
if a>15 and a<20:
    print("Both are true") #OUTPUT:-Both are true

#---------------------------------------------------------------------
#---or With if
"""At least one condition must be True.
    same example on 'and with if'. """

#---------------------------------------------------------------------
#---not With if
"""not reverses True/False."""

#---------------------------------------------------------------------
#---Nested if
"""An if inside another if. """ 