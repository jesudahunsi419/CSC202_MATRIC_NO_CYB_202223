import random
test_sed = int(input("Create a seed number: "))
random.seed(test_sed)
Afg =random.randint(0,1)
if Afg== 1:
    print("Heads")
else :
    print("Tails")

# BANKER ROULETTE
print("You are at a bar with your friends, who will buy the meat?")
nameAsv= input("Give me your names").lower()
faDg= nameAsv.split()
no_item=len(faDg)
As1= random.randint(0,no_item - 1)
per3=faDg[As1]
# As1= random.choice(faDg)
#asF= faDg[As1]
print(f"{per3} is going to buy the meat today")
# print(f"{As1} is going to buy the meat today")
# # print(f"{faDg}")

 # ROCK PAPER SCISSORS
  # FINAL PROJECT
rock ='''
       _______
__'     _______)
       (______) 
       (______)
       (_____) 
^^^'__ (____)
'''

paper= '''
   _______
__'  _____)
        ______) 
           ______)
          _____) 
^^^'__   ____)
'''
scissors ='''
   _______
__'  _____)___
        ______) 
         ______)
        (__) 
^^^'__  (__)
'''
#print (scissors)
Dah= input(" What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
if len(Dah)>1:
     print("stop, read the instructions clearly")
HaDf = int(Dah)
CHOIce=[rock,paper, scissors]
Computer_C=random.randint(0,2)
# print(f"The Computer chose {Computer_ch}")
Computer_ch=CHOIce[Computer_C]
HaD=CHOIce[HaDf]
print(f"The Computer chose {Computer_ch}")
print(HaD)

if Computer_ch == rock and HaD == scissors:
    print("Computer Wins")
elif Computer_ch == scissors and HaD ==paper:
    print("Computer wins")
elif Computer_ch == paper and HaD ==rock:
     print("Computer wins")
elif Computer_ch == HaD :
    print("Draw")
    #if HaD == 0 and Computer_ch == 2 :
    #   print("You win")
elif Computer_ch == paper and HaD ==scissors:
     print("You win")
elif Computer_ch == scissors and HaD ==rock:
     print("You win")

elif Computer_ch == rock and HaD ==paper:
     print("You win")