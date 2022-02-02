############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
##cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os
from art import logo

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#List of Cards. 11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#deal_card() function that uses the List to *return* a random card.
def deal_card():
  """Returns a random card from the deck."""
  return random.choice(cards)

#calculate_score() that takes a List of cards as input and returns the score. 
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  #calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  #check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

#function to compare(). Pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  """Compare user score and computer scroe to determine winner"""
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Computer Wins"
  elif user_score == 0:
    return "Black Jack!!! You win!"
  elif user_score > 21:
    return "You went over. You lose!"
  elif computer_score > 21:
    return "Computer went over. Computer Loses"
  elif user_score > computer_score:
      return "You win!"
  else:
      return "You lose!"

def play_game():
  print(logo)
  #Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  computer_cards = []
  is_game_over = False

  user_cards.append(deal_card())
  user_cards.append(deal_card())

  computer_cards.append(deal_card())
  computer_cards.append(deal_card())

  while not is_game_over:
    #The score is rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your hand: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      #If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_choice == 'y':
        user_cards.append(deal_card())
        print(user_cards)
        print(computer_cards)
      else:
        is_game_over = True

  #Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
    print(f"Computer: {computer_cards} totals {computer_score}")

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))


#Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clearConsole()
  play_game()
