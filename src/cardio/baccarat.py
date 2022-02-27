from .deck import Deck
import json


class Baccarat:
  def __init__(self, deck=None):
    self.deck = list(deck if deck else Deck(n_decks=8, baccarat=True))
    self.discard = []

  sum_cards = staticmethod(lambda cards: sum(x.game_value for x in cards) % 10)

  def simulate_play(self):
    while len(self.deck) > 6:
      yield self.play()

  def discard_cards(self):
    self.discard.extend(self.player)
    self.discard.extend(self.banker)

  def play_bet(self, bets):
    '''
    Bets will come in the form of:
    [{
      'player': float,
      'banker': float,
      'tie': float
    }]
    
    Results will include the winning slot only with the value won or zero
    input: [{'player': 3, 'banker': 0, 'tie': 0}, {'player': 0, 'banker': 5, 'tie': 0}]
    output: [{"banker": 0.0}, {"banker": 4.75}]
    
    '''
    # payout for wins on player are 1:1
    # payout for wins on banker are 19:20 - 5% is deducted on cash-out (this will do it automatically)
    # payout for wins on tie are 8:1
    winner = self.play()['winner']
    payout_map = {
      'tie': 9,
      'player': 2,
      'banker': 1.95    # some pay 0.5:1 for any banker win with a value of 6 (and 1:1 otherwise)
    }

    return list(map(
      lambda x: {
        winner: (x[winner] * payout_map[winner]) if winner != 'tie' else (x['banker'] + x['player'])
      },
      bets
    ))

  def play(self):
    self.player = []
    self.banker = []
    
    def announce(winner):
      self.discard_cards()
      return {
        'winner': winner,
        'player': {'hand': [repr(x) for x in self.player], 'score': self.player_score},
        'banker': {'hand': [repr(x) for x in self.banker], 'score': self.banker_score},
        'cards_left': len(self.deck),
        'discard_size': len(self.discard)
      }
    
    # deal cards
    self.player += [self.deck.pop(0)]
    self.player += [self.deck.pop(0)]
    self.banker += [self.deck.pop(0)]
    self.banker += [self.deck.pop(0)]
    
    # sum card values
    self.player_score = self.sum_cards(self.player)
    self.banker_score = self.sum_cards(self.banker)
    
    # apply draw rules to player
    
    if self.player_score in [8, 9] and self.player_score > self.banker_score:
        # player wins
      return announce('player')
    elif self.banker_score in [8, 9] and self.banker_score > self.player_score:
      # banker wins
      return announce('banker')
    
    player_draw = None
    if self.player_score < 6:
      self.player += [self.deck.pop(0)]
      self.player_score = self.sum_cards(self.player)
      
      player_draw = self.player[-1].game_value
      
    # apply draw rules to banker
    if self.banker_score in [0, 1, 2]:
      self.banker += [self.deck.pop(0)]
    elif self.banker_score == 3 and player_draw in [0, 1, 2, 3, 4, 5, 6, 7, 9, None]:
      self.banker += [self.deck.pop(0)]
    elif self.banker_score == 4 and player_draw in [2, 3, 4, 5, 6, 7, None]:
      self.banker += [self.deck.pop(0)]
    elif self.banker_score == 5 and player_draw in [4, 5, 6, 7, None]:
      self.banker += [self.deck.pop(0)]
    elif self.banker_score == 6 and player_draw in [6, 7]:
      self.banker += [self.deck.pop(0)]
      
    self.banker_score = self.sum_cards(self.banker)

    if self.player_score == self.banker_score:
      return announce('tie')
    if self.player_score in [8, 9] and self.player_score > self.banker_score:
      # player wins
      return announce('player')
    elif self.banker_score in [8, 9] and self.banker_score > self.player_score:
      # banker wins
      return announce('banker')
    else:
      return announce('player' if self.player_score > self.banker_score else 'banker')


if __name__ == "__main__":
  game = Baccarat()
  for x in game.simulate_play():
    print(json.dumps(x))
