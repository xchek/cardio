suits = {'spade': 'S', 'club': 'C', 'heart': 'H', 'diamond': 'D'}
suit_chars = {'S': '\u2660', 'C': '\u2663', 'H': '\u2665', 'D': '\u2666'}

high_card_values = {11: 'jack', 12: 'queen', 13: 'king', 1: 'ace'}

high_cards = {'jack': 'J', 'queen': 'Q', 'king': 'K', 'ace': 'A'}

baccarat_map = {10: 0, 11: 0, 12: 0, 13: 0}

blackjack_map = {11: 10, 12: 10, 13: 10, 1: 11}

invert = lambda d: {v: k for k, v in d.items()}

suit_names = invert(suits)
high_card_values_ = invert(high_card_values)


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

  def __init__(self, suit=None, value=None, baccarat=False):
    _suit = suits.get(suit.lower()) or suit_names.get(suit.upper())
    suit_name = suit_names.get(_suit, _suit)
    assert suit_name, f"Suit must be one of: Spade, Heart, Diamond, Club :: Provided Value: {suit}"
    self.suit_short = suits.get(suit_name)
    self.suit = suit_name
    self.suit_char = suit_chars.get(self.suit_short)

    assert 1 <= value <= 13, "Cards value must be an int 1-13"
    self.value = value
    self.game_value = value if not baccarat else baccarat_map.get(value, value)
    face_value = high_card_values.get(value, value)
    self.face_value_short = high_cards.get(face_value, face_value)

  def __repr__(self):
    return f"<{self.face_value_short}{self.suit_char}>"

  def __add__(self, o):
    return self.game_value + o.game_value
