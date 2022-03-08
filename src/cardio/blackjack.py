from .deck import Deck
import json


class Blackjack:
  '''
  Actions:
    Split
    Double Down
    Stand
    Hit
    Insure
  
  Dealer stands with 17
  
  Primary deal order:
    player
    dealer
    player
    dealer
  
  '''
  def __init__(self, deck=None, players=[]):
    self.deck = list(deck if deck else Deck(n_decks=6, blackjack=True))
    self.discard = []
    self.players = players
    self.dealer = []

  def simulate_play(self):
    while len(self.deck) > 6:
      yield self.play()

  def discard_cards(self):
    for player in self.players:
      self.discard.extend(player['hand'])
    self.discard.extend(self.dealer)

  def sum_cards(self, cards):
    totals = [0]
    i = 1
    for card in cards:
      for ix in range(i):
        totals[ix] += card.game_value
      if card.game_value == 11:
        totals.append(totals[i - 1] - 10)
        i += 1
    return [x for x in totals if x <= 21]
  
  def sum_dealer_cards(self, cards):
    first_ace = False
    result = 0
    for card in cards:
      if card.game_value == 11 and not first_ace:
        if not first_ace:
          first_ace = True
        else:
          card.game_value = 1
      result += card.game_value
    return result

  def pay_winnings(self):
    dealer_sum = self.sum_dealer_cards(self.dealer)
    for player in self.players:
      if (21 in player['hand_sums'] and dealer_sum != 21):
        player['winnings'] = player['bet'] * 2.5
      elif any(x > dealer_sum for x in player['hand_sums']):
        player['winnings'] = player['bet'] * 2
      del player['bet']

  def play(self):
    self.dealer = []
    # generator of cards for player?
    for player in self.players:
      player['hand'] = [self.deck.pop(0)]
    
    self.dealer.append(self.deck.pop(0))
    
    for player in self.players:
      player['hand'] += [self.deck.pop(0)]

    hidden_second_dealer_card = self.deck.pop(0)    # maybe shouldn't yield this card yet - players bet on the dealer's one face up card

    for player in self.players:
      while hand_sums := self.sum_cards(player['hand']):
        player['hand_sums'] = hand_sums
        if 21 in hand_sums:
          break
        action = yield {**player, 'dealer_hand': self.dealer, 'option': True}
        if not action:
          continue
        if action.lower() in ['hit', 'h']:
          player['hand'] += [self.deck.pop(0)]
        elif action.lower() in ['stand', 's']:
          break
        elif action.lower() in ['split']:
          ...
    
    self.dealer.append(hidden_second_dealer_card)
    
    while self.sum_dealer_cards(self.dealer) < 17:
      self.dealer += [self.deck.pop(0)]

    self.pay_winnings()

    yield {'result': True, 'dealer_hand': self.dealer, 'players': self.players, 'dealer_sum': self.sum_dealer_cards(self.dealer)}
