from .card import Card, suits
import random


class Deck:
  def __init__(self, ordered_deck=False, n_decks=1, baccarat=False):
    self.cards = [
      Card(suit, card_value, baccarat)
      for deckn in range(n_decks)       # baccarat & other games use multiple decks
      for suit in suits
      for card_value in range(1, 14)
    ]
    self.shuffle() if not ordered_deck else None

  def __iter__(self):
    return self

  def __next__(self):
    '''
    Allows iterating the deck - but does not keep track of "discarded" cards.
    
    Can use Deck like:
    for card in Deck():
      ...
    '''
    if self.cards:
      return self.cards.pop(0)
    else:
      raise StopIteration
  
  def __repr__(self):
    return f"<Deck size={len(self.cards)}>"

  def shuffle(self, n_times=1):
    [random.shuffle(self.cards) for x in range(n_times)]
