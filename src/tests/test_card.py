import unittest

from cardio import Card



class TestCard(unittest.TestCase):
  def test_card_sum(self):
    result = Card('spade', 1) + Card('heart', 5)
    self.assertEqual(result, 6)

    result = Card('s', 1) + Card('h', 1)
    self.assertEqual(result, 2)

  def test_card_assertions(self):
    with self.assertRaises(AssertionError):
      Card('not club', 3)

    with self.assertRaises(AssertionError):
      Card('h', 15)

  def test_baccarat_values(self):
    for case, expected_result in [
      ({'suit': 'd', 'value': 10, 'baccarat': True}, 0),
      ({'suit': 's', 'value': 11, 'baccarat': True}, 0),
      ({'suit': 'c', 'value': 12, 'baccarat': True}, 0),
      ({'suit': 'h', 'value': 13, 'baccarat': True}, 0),
      ({'suit': 'd', 'value': 10, 'baccarat': False}, 10),
      ({'suit': 's', 'value': 11, 'baccarat': False}, 11),
      ({'suit': 'c', 'value': 12, 'baccarat': False}, 12),
      ({'suit': 'h', 'value': 13, 'baccarat': False}, 13),
    ]:
      card = Card(**case)
      self.assertEqual(card.game_value, expected_result, msg=f"{card.game_value=} {expected_result=} {case=}")

  def test_repr(self):
    card = Card('spade', 3)
    result = card.__repr__()
    self.assertEqual(result, '<3\u2660>')
