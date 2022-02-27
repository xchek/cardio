
suits = {'spade': 'S', 'club': 'C', 'heart': 'H', 'diamond': 'D'}

high_card_values = {11: 'jack', 12: 'queen', 13: 'king', 1: 'ace'}

high_cards = {'jack': 'J', 'queen': 'Q', 'king': 'K', 'ace': 'A'}

baccarat_map = {10: 0, 11: 0, 12: 0, 13: 0}

blackjack_map = {11: 10, 12: 10, 13: 10, 1: 11}


class Card(object):
  """
  
  Card "values" are assigned from deck.py as follows:
  ace = 1
  2, 3, 4, 5, 6, 7, 8, 9, 10
  j = 11
  q = 12
  k = 13
  
  This uses self.game_value to differ from the "face value" 
  and the value the game assigns to the card.
  """
  
  def __init__(self, symbol=None, value=None, baccarat=False):
    self.suit = symbol
    self.suit_short = suits[symbol]
    self.value = value
    self.game_value = value if not baccarat else baccarat_map.get(value, value)
    face_value = high_card_values.get(value, value)
    self.face_value_short = high_cards.get(face_value, face_value)
  
  def __repr__(self):
    return f"{self.face_value_short}-{self.suit_short}"

  def __add__(self, o):
    return self.game_value + o.game_value
