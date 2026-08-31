#-------------------------------------------------------------------------------------
#-------------------FIRST PROBLEM IN PYTHON 
#-Ball and Bat Price Calculator
Ball_Price = 50
Bat_price = 20

number_of_ball = int(input("how many ball you will buy: "))
number_of_bat = int(input("how many Bat you will buy: "))

ball_total = Ball_Price * number_of_ball
bat_total =  Bat_price * number_of_bat

Total_Price = ball_total + bat_total 

print("Total Ball Price:", ball_total)
print("Total Bat Price:", bat_total)
print("Total Price:",Total_Price  ) 
print("\n\n\n")
#-------------------------------------------------------------------------------------------


#--Discount Price Calculator
pen_box = 150
pencil_box = 50
discount = 20

price = pen_box +  pencil_box

#-- discount formula 
discount_price = price *(1 - discount / 100) 

print ("total price:", discount_price)

#----------------------------------------------------------------------------------------------

#--Minutes to Hours Converter
minutes = int(input("no.of minutes:"))

hours = minutes // 60
reamaing_minutes = minutes % 60 
print ("hours:", hours)
print("reamaing_minutes:", reamaing_minutes)
print("\n\n\n")
#-------------------------------------------------------------------------------------------------

#--Basket Calculator
total_apple = 47 
apple_basket = 47 // 6
Remaining_apples = 6 % 47 

print( "apple_basket", apple_basket)
print("Remaining_apples", Remaining_apples)

#------------------------------------------------------------------------------------------------

