import random
word_list=["arshavin", "baboon", "duck"]
chosen_word = random.choice(word_list)
end_of_game = True

geses=6
display= []
Gaya= len(chosen_word)
for letter in range (Gaya) :
        display += "_"
    
while end_of_game:
    guesss= input("Guess a letter").lower()
    

    # for letter in chosen_word :
    #print(display)
        
    for position in range(Gaya) :
        letter = chosen_word[position]
        if letter== guesss :
    # display+= guesss
            display[position]= letter
        else:
            geses-=1

    print(display)

    if "_" not in display :
      end_of_game = False
      print(f" You won")
    elif geses==0 :
        end_of_game= False

# for letter in chosen_word :
    #     if letter == guesss :
    #         print("Right")
    #     else :
    #         print("Wrong")


