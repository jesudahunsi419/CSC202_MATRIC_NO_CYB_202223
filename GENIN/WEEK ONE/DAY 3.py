# ODD or EVEN NUMBERS CHECKER
# TEST FOR EVEN OR ODD NUMBERS
number = int(input("Which number do you want to choose?"))
if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

# BMI 2.0
print(" Welcome to BMI 2.0")
height = float(input("enter your height in m:"))
weight = float(input("enter your weight in kg"))
B_M = round(weight / (height ** 2), 1)
if B_M < 18.5:
    print("you are underweight")
elif B_M < 25:
    print("you have a normal weight")
elif B_M < 30:
    print("you are overweight")
elif B_M < 35:
    print("You are obese")
elif B_M > 35:
    print("You are clinically obese")
else:
    print("Daffodil")

# CHECK FOR LEAP YEAR
year = int(input(" Which year do you want to check?"))
if year % 4 == 0:
    print("leap year")
elif year % 100 == 0:
    print(" not leap year")
elif year % 400 == 0:
    print("leap year")
else:
    print(" not leap year")

#Pizza Ordering Service
print("Welcome to the pizza delivery!")
size = input(" What size of pizza do you want? S, M or L").upper()
add_peproni = input(" Do you want pepperoni? Y or N").upper()
extwches = input("Do you want extra cheese? C or N").upper()
bill = 0

if size == "S":
    bill += 15

elif size == "M":
    bill += 20

elif size == "L":
    bill += 25
else:
    print(" check the metrics")

if add_peproni == "Y" and size == "S":
    bill += 2
else:
    bill += 3

if extwches == "C":
    bill += 1
    print(f" Your final bill is ${bill}")
else:
    print(f" Your final bill is  ${bill}")

# LOVE CALCULATOR
print(" Welcome to the Love Calculator")
nam1 = input("What is your name?\n").lower()
nam2 = input("What is your name?\n").lower()

A = nam1.count("l")
F = nam1.count("o")
M =nam1.count("v")
G = nam1.count("e")
F1st =str(A+F+M+G)

S = nam2.count("l")
D = nam2.count("o")
K=  nam2.count("v")
L = nam2.count("e")
H2r =str(S+D+K+L)
#print (type(nam2))
prE = int((F1st) + H2r)
if prE < 10 or prE > 90 :
    print(f"Your score is{prE}, you go together like coke and mentos")
    if 40 < prE < 50:
        print(f"Your score is {prE}, you are alright together")
else:
        print(f"Your score is {prE}")

#TREASURE ISLAND
print("Welcome to the treasure island")
import random

print("Your mission is to find the treasure")
op = input(" You're at cross road, choose left or right!").lower()
Comp_ch = random.randint(0, 3)
gift = ["yellow", "green", "red"]
gik = gift[Comp_ch - 1]
if op == "left":
    # print(" continue the game")
    griM = input(" You've come to a lake, swim or wait?").lower()

    if griM == "wait":
        final = input(
            "you arrive at the island. there are three different colors of door red, yellow and blue. pick one color").lower()
        if final == gik:
            print("You Win!")
        else:
            print(" game Over")

    else:
        print(" you were ambushed, game over")

else:
    print(" game OvEr")
