import unittest

from cardio import Card



class TestCard(unittest.TestCase):
  def test_card_sum(self):
    result = Card('spade', 1) + Card('heart', 5)
    self.assertEqual(result, 6)
