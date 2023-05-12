import random

def deal_card():
  """"Outputs random card from list of cards"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def check_score(cards):
  """"Returns sum/score of given hand of cards"""
  if sum(cards) == 21 and len(cards) == 2:
    # 0 will represent a hand of Blackjack
    return 0
  if sum(cards) > 21 and 11 in cards:
    # The number 11 represents an Ace, which can have value of 11 or 1
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def comprare_scores(user_score, computer_score):
  if user_score == computer_score:
    return "It's a draw!"
  elif user_score == 0:
    return "You have blackjack, you win!"
  elif computer_score == 0:
    return "The house has blackjack, you lose."
  elif user_score > 21:
    return "You went over 21, you lose."
  elif computer_score > 21:
    return "Your opponen went over 21, you win!"
  elif user_score > computer_score:
    return "You win!"
  else:
    "You lose."

user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())
  
while not is_game_over:
  user_score = check_score(user_cards)
  computer_score = check_score(computer_cards)
  
  print(f"Your cards: {user_cards}, your score: {user_score}")
  print(f"Computer's first card: {computer_cards[0]}")

  if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
  else: 
    deal_new = input("Do you want another card? Y/n\n")
    if deal_new == "n":
      is_game_over = True
    else:
      user_cards.append(deal_card())

while computer_score < 17 and computer_score != 0:
  computer_cards.append(deal_card())
  computer_score = check_score(computer_cards)

print(comprare_scores(user_score, computer_score))