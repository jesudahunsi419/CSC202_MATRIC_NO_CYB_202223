# DATA TYPE
Number= input("Enter your Number")
number_1=int(Number[0])
number_2= int(Number[1])
print(number_1+number_2)

#BMI CALCULATOR
height = float(input("enter your height in m:"))
weight= float(input("enter your height in kg:"))
BMI= weight // (height*height)
print(int(BMI))

#LIFE IN WEEKS
age= int(input("What is your age?"))
Days= (90-age)*365
Weeks= (90-age)*52
Month=(90-age)*12
print(f"You have {Days}days, {Weeks}weeks and {Month}months left")

#TIP CALCULATOR
print("Welcome to the tip Calculator")
BLi= float(input("What was the Total bill?"))
tip= int(input(" What percentage tip would you like to give? 10, 12 or 15?"))
Uf= input("How many people to split the bill?")
MU=tip/100
people=int(Uf)
TRy=(round((BLi*MU+BLi)/people,2))
print(f"Each person should pay: ${TRy}")