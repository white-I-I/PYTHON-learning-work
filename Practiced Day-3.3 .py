
#--Password Login Checker
password = "MY_FIRST_PASSWORD"
Login_password = input("Enter Your Password:") 

if Login_password == password: # input text first(Login_password) after that (password)
    print("Login successful")
else:
    print("wrong password")

print("\n")

#----------------------------------------------------------------

#--Simple Password Verification
user_pass = "pass123"

if user_pass == "pass123":
    print ("correct")

#-------------------------------------------------------------------

#--Age Comparison Checker
age = 20
if age != 18: #(not equal)
    print("Age is not 18")
print("\n")

#--------------------------------------------------------------

#--Student Grade Calculator
Student_marks = int(input("Enter The Marks:"))

if Student_marks >= 90:
    print("A GRADE [congratulation party🥳🥳🎉]") 
elif Student_marks >= 75:   
    print("B GRADE [kk, man keep it up]")
elif Student_marks >=60:
    print("C GRADE ")
elif Student_marks >=40:
    print("D GRADE [mom party 🥶🥶]")
else:
    print ("FAIL MAN [BAD LUCKY😞]")  
print("\n")

#----------------------------------------------------------------

#-Positive, Negative or Zero Checker
number = int(input("Enter The Number:"))

if number > 0:
    print("POSITIVE MARKS")
elif number == 0:
    print("ZERO MARKS")
else:
    print("NEGITIVE MRAKS")
print("\n") 

#----------------------------------------------------------------

#--Bank Withdrawal Calculator
my_amount = 10000 

withdraw_amount = int(input("Enter your withdraw amount:"))
TOTAL = my_amount - withdraw_amount

if withdraw_amount <= my_amount:
    print("Withdraw successful: ", withdraw_amount)
    print(" Remaining balance: ", TOTAL)  
else:
    print ("withdraw Fail /'insufficient balance ")     

#--------------------------------------------------------------------

#--Even or Odd Number 
number = int(input("Enter your numder:"))

if number % 2 == 0: 
    print ("even numder")
elif number % 2 == 1:
    print("odd numder")

#-----------------------------------------------------------------

#--Age Ticket Price Calculator
age = int(input("Enter your age: "))
Tickets = int(input("Enter no.of tickets: "))

if age <10:
    price = 50
elif age <20:
    price = 100
elif age < 35:
    price = 300
else:
    price = 200

total = price * Tickets

print("ticket price: ",price) 
print("no.of ticket price: ",Tickets)
print("total price:", total) 

#---------------------------------------------------------------------

#--Shopping Discount Calculator
price1 = float(input("Product 1 price: ₹"))
price2 = float(input("Product 2 price: ₹"))
price3 = float(input("Product 3 price: ₹"))
subtotal = price1 + price2 + price3

if subtotal < 1000:
    discount_rate = 0
elif subtotal < 5000:
    discount_rate = 0.10
else:
    discount_rate = 0.20

discount = subtotal * discount_rate
final_price = subtotal - discount

print("Subtotal: ₹", subtotal)
print("Discount: ₹", discount)
print("Final price: ₹", final_price)

#---------------------------------------------------------------------
#-example
n = 16

age = "adult" if n>17 else "minor"
print(age)

#---------------------------------------------------------------------
#-Triangle 
a = 7
b = 6
c = 7
if a==b==c:
  print("Equilateral")
elif a==b!=c or a!=b==c:
  print("Isosceles")
else:
  print("Scalene")

#-----Temperature Converter-----------------------------------------------

choice = input("if you choice Celsius type 'C' or if you choice is Fahrenheit type 'F':").upper()
#.upper() - means convert into capital letters

if choice == 'C':
    celsius = float(input("Enter Celsius"))
    Fahrenheit = (celsius * 9/5) + 32
    print(Fahrenheit)
elif choice == 'F':
    Fahrenheit = float(input("Enter Fahrenheit"))
    celsius = (Fahrenheit - 32) * 5/9
    print(celsius)
else:
    print("invaid choice") 

#----positive,negative and zero---------------------------------------
n = int(input("input"))
if n>=1:
    print("positive")
elif n<0:
    print("negative")
else:
    print("zero")

#---Largest of Two Numbers-------------------------------------------
a = int(input("Enter a:"))
b =int(input("Enter b:"))

if a>b:
    print("a is biggest", a)
else:
    print("b is biggestn", b)

#---Divisibility--------------------------------------------------------------
n = int(input("Enter the number: "))

if  n % 2 == 0:
    print("Divisible by 2")
    if n % 3 ==0:
        print("Divisible by 3")
        if n % 5 ==0:
            print("Divisible by 5")
            if n % 7 ==0:
                print("Divisible by 7")
            else:
                print("Not divisible by 7")
        else:
            print("Not divisible by 5")
    else:
        print("Not divisible by 3")
else:
    print("Not divisible by 2")


#--Login System------------------------------------------------------------
username = "python"
password = "python123"

user_username=str(input("Enter username: "))
user_password=str(input("Enter password: "))

if username == user_username and password == user_password:
    print("login successfull ")
else:
    print("login failed")