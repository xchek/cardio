from cardio.blackjack import Blackjack
from cardio import Card

if __name__ == "__main__":
  players = [
    {
      'name': 'Franklin',
      'bet': 25.0
    },
    {
      'name': 'Anna',
      'bet': 50.0
    }
  ]
  game = Blackjack(players=players)
  # result = game.sum_cards([Card('s', 1, blackjack=True), Card('h', 1, blackjack=True)])
  # print(f"{result=}")
  round = game.play()
  action = next(round)
  while True:
    if action.get('option'):
      action = round.send(input(f"{action=} Choice?"))
    if action.get('result'):
      break
  print(action)
