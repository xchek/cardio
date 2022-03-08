import json
import sys
from collections import Counter

from cardio.baccarat import Baccarat

if __name__ == "__main__":
  # SHUFFLES = 1000
  SHUFFLES = int(sys.argv[-1])
  count = Counter()
  for x in range(SHUFFLES):
    game = Baccarat()
    for outcome in game.simulate_play():
      count[outcome['winner']] += 1
    del game
  total_games = sum(count.values())
  results = {k: v / total_games for k, v in count.items()}
  print(json.dumps({**results, 'shoe_shuffles': SHUFFLES, 'games': total_games}))



# https://bodhi-root.github.io/gambling-stats-bookdown/baccarat.html
# https://www.tandfonline.com/doi/full/10.1080/14459795.2020.1817969
# "The statistical win frequencies are as follows for eight-deck baccarat:
#     44.62% for players      +
#     45.86% for bankers      +
#      9.52% for ties         +
#      7.47% for pairs"       -  (excluded from percent)

# v6 - This is more like the above noted values.
# More understanding about the order of operations in a game of baccarat was needed.
# https://www.fgbradleys.com/rules/rules4/Baccarat%20-%20rules.pdf
# {"player": 0.4470018134506982,  "banker": 0.45825887158539697, "tie": 0.09473931496390478, "shoe_shuffles": 10000,   "games": 834321}
# {"player": 0.44593519911659024, "banker": 0.45878709505440823, "tie": 0.09527770582900152, "shoe_shuffles": 100000,  "games": 8343127}
# {
#   "player": 0.446270768805319,
#   "banker": 0.45856084295259514,
#   "tie": 0.09516838824208584,
#   "shoe_shuffles": 1000000,
#   "games": 83430172  # computer has a serious gambling problem
# }

# v5 - Bug returning a banker win when it was actually a player win (fix shifted 2% from player to banker).
# {"player": 0.4689103831817147, "banker": 0.4361391775436578, "tie": 0.09495043927462754, "shoe_shuffles": 10000,  "games": 834330}
# {"player": 0.4691322082109634, "banker": 0.4358139809720742, "tie": 0.09505381081696244, "shoe_shuffles": 100000, "games": 8343211}

# v4
# {"player": 0.4584594136480633,  "banker": 0.42580199635884236, "tie": 0.11573858999309436, "shoe_shuffles": 1000,   "games": 79645}
# {"player": 0.4598056653532781,  "banker": 0.4268558883448166,  "tie": 0.11333844630190532, "shoe_shuffles": 10000,  "games": 796667}
# {"player": 0.45975724513721267, "banker": 0.4271218765007392,  "tie": 0.11312087836204814, "shoe_shuffles": 100000, "games": 7964825}

# v3
# {"player": 0.4525454109534302,  "banker": 0.40827044491888254, "tie": 0.13918414412768726, "shoe_shuffles": 1000,   "games": 87589}
# {"player": 0.4515491048196401,  "banker": 0.4089686937944509,  "tie": 0.139482201385909,   "shoe_shuffles": 10000,  "games": 876248}
# {"player": 0.45162694344746335, "banker": 0.40898062421065856, "tie": 0.1393924323418781,  "shoe_shuffles": 100000, "games": 8762843}

# v2
# {"player": 0.5098386635265115, "banker": 0.3529372922765391,  "tie": 0.13722404419694936, "shoe_shuffles": 1000,   "games": 90866}
# {"player": 0.5130050841156036, "banker": 0.35074787758523207, "tie": 0.13624703829916424, "shoe_shuffles": 10000,  "games": 909106}
# {"player": 0.5125018811235522, "banker": 0.35123117886382776, "tie": 0.13626694001262002, "shoe_shuffles": 100000, "games": 9090312}

# v1 - Does not match up to known odds...
# {"player": 0.5388494771879098, "banker": 0.3714599513611046,  "tie": 0.08969057145098566, "shoe_shuffles": 1000,   "games": 89229}
# {"player": 0.5384686892399222, "banker": 0.37225935649197633, "tie": 0.08927195426810146, "shoe_shuffles": 10000,  "games": 892856}
# {"player": 0.5383698884818724, "banker": 0.3725007130221985,  "tie": 0.08912939849592909, "shoe_shuffles": 100000, "games": 8930297}

