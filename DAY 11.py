##### Blackjack Project #######

#Difficulty Normal: Use all Hints below to complete the project.
#Difficulty Hard: Use only hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard: only use Hints 1 & 2 to complete the project.
#Difficulty Expert: Only use Hint 1 to complete the project.
########## Our Blackjack House Rules ##########
## The deck is unlimited in size.
##There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of card:
cards= [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
##The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
########## Hints ##########
# Hint 1: Go to this website and try out the Blackjack game:
# https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
# https://blackjack-final.appbrewery.repl.run
import random
def deal_card():
    """Returns  a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card =random.choice(cards)
    return card
def calculate_score(cards):
user_cards = []
computer_cards = []
is_game_over = False
for _ in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f" Your cards: {user_cards}, current score: {user_score}")
print(f" Computer's first card: {computer_cards[0]}")
if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
            user_cards.append(deal_card())
      else:
            is_game_over = True
            

def calculate_score(user_cards):
       return sum(cards)
if sum(cards) == 21 and len(cards) == 2:
      return 0
if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
      return sum(cards)