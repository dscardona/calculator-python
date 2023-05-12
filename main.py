# Deal card function
import random

def deal_card():
  """"outputs random card from list of cards"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)
