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

user_cards = []
computer_cards = []

for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

