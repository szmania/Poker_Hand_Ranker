###
# Created by Curtis Szmania
# Date: 06/10/17
# Comment: comScore coding assessment test.
# Runs rankHand 100,000 times to test output.
###

__author__ = 'szmania'

from random import randint
from rankHand import Card, RankHand, setup_logger

def no_duplicates(args):
    """
    Sees if arguments have no duplicates

    :param args:  Dictionary of tuples of cards. ie:.
    :type args: Dictionary.
    """

    for arg1 in args:
        card1 = args[arg1]

        for arg2 in args:
            card2 = args[arg2]

            if card1 == card2 and not arg1 == arg2:
                return False

    return True

def test_all_ranks():
    """
    Tests all ranks.
    """

    print('1. Royal Flush')
    kwargs = {'card1': ['K','S'],
              'card2': ['Q','S'],
              'card3': ['A','S'],
              'card4': ['10','S'],
              'card5': ['J','S']
              }
    royalFlush = RankHand(logLevel='INFO', **kwargs)
    rank = royalFlush.getRank()
    print('Rank %d\n' % rank)

    print('2. Straight Flush')
    kwargs = {'card1': ['8','S'],
              'card2': ['J','S'],
              'card3': ['7','S'],
              'card4': ['10','S'],
              'card5': ['9','S']
              }
    straightFlush = RankHand(logLevel='INFO', **kwargs)
    rank = straightFlush.getRank()
    print('Rank %d\n' % rank)

    print('3. Four of a Kind')
    kwargs = {'card1': ['4','C'],
              'card2': ['4','S'],
              'card3': ['2','C'],
              'card4': ['4','D'],
              'card5': ['4','H']
              }
    fourOfAKind = RankHand(logLevel='INFO', **kwargs)
    rank = fourOfAKind.getRank()
    print('Rank %d\n' % rank)

    print('4. Full House')
    kwargs = {'card1': ['2','C'],
              'card2': ['2','S'],
              'card3': ['4','C'],
              'card4': ['4','D'],
              'card5': ['4','H']
              }
    fullHouse = RankHand(logLevel='INFO', **kwargs)
    rank = fullHouse.getRank()
    print('Rank %d\n' % rank)

    print('5. Flush')
    kwargs = {'card1': ['2','C'],
              'card2': ['7','C'],
              'card3': ['4','C'],
              'card4': ['J','C'],
              'card5': ['5','C']
              }
    flush = RankHand(logLevel='INFO', **kwargs)
    rank = flush.getRank()
    print('Rank %d\n' % rank)

    print('6. Straight')
    kwargs = {'card1': ['2','C'],
              'card2': ['4','S'],
              'card3': ['3','D'],
              'card4': ['6','S'],
              'card5': ['5','C']
              }
    straight = RankHand(logLevel='INFO', **kwargs)
    rank = straight.getRank()
    print('Rank %d\n' % rank)

    print('7. Three of a Kind')
    kwargs = {'card1': ['A','C'],
              'card2': ['5','S'],
              'card3': ['2','D'],
              'card4': ['2','S'],
              'card5': ['2','C']
              }
    threeOfAKind = RankHand(logLevel='INFO', **kwargs)
    rank = threeOfAKind.getRank()
    print('Rank %d\n' % rank)

    print('8. Two Pairs')
    kwargs = {'card1': ['A','C'],
              'card2': ['J','S'],
              'card3': ['J','C'],
              'card4': ['K','S'],
              'card5': ['K','C']
              }
    twoPair = RankHand(logLevel='INFO', **kwargs)
    rank = twoPair.getRank()
    print('Rank %d\n' % rank)

    print('9. Pair')
    kwargs = {'card1': ['A','C'],
              'card2': ['5','S'],
              'card3': ['J','C'],
              'card4': ['2','S'],
              'card5': ['2','C']
              }
    pair = RankHand(logLevel='INFO', **kwargs)
    rank = pair.getRank()
    print('Rank %d\n' % rank)

    print('10. High Card')
    kwargs = {'card1': ['A','C'],
              'card2': ['5','S'],
              'card3': ['J','C'],
              'card4': ['K','S'],
              'card5': ['2','C']
              }
    highCard = RankHand(logLevel='INFO', **kwargs)
    rank = highCard.getRank()
    print('Rank %d\n' % rank)



def main():
    """
    Run brute-force test for rankHand giving 1000 random hand types.
    """

    setup_logger()

    test_all_ranks()

    suites = Card.get_suites()
    types = Card.get_types()

    kwargs = {}

    PASS = 0
    FAIL = 0
    TOTAL = 0
    ranks = {1:0,
             2:0,
             3:0,
             4:0,
             5:0,
             6:0,
             7:0,
             8:0,
             9:0,
             10:0
             }

    for i in range(0, 100000):
        kwargs['card1'] = ['%s' % types[randint(0, len(types) - 1)], '%s' % suites[randint(0, len(suites) - 1)]]
        kwargs['card2'] = ['%s' % types[randint(0, len(types) - 1)], '%s' % suites[randint(0, len(suites) - 1)]]
        kwargs['card3'] = ['%s' % types[randint(0, len(types) - 1)], '%s' % suites[randint(0, len(suites) - 1)]]
        kwargs['card4'] = ['%s' % types[randint(0, len(types) - 1)], '%s' % suites[randint(0, len(suites) - 1)]]
        kwargs['card5'] = ['%s' % types[randint(0, len(types) - 1)], '%s' % suites[randint(0, len(suites) - 1)]]

        if no_duplicates(kwargs):
            TOTAL =  TOTAL + 1
            try:
                rankObj = RankHand(logLevel='INFO', **kwargs)
                rank = rankObj.getRank()
                print('Hand: %s' % rankObj.hand.str)
                print('Rank %d\n' % rank)

                if rank:
                    PASS = PASS + 1
                    ranks[rank] = ranks[rank] + 1
            except:
                FAIL = FAIL + 1

    print('TOTAL RUNS: %d' % TOTAL)
    print('Total Pass: %d' % PASS)
    print('Total Fail: %d' % FAIL)

    for item in ranks:
        print('Rank %d: %d' % (item, ranks[item]))

if __name__ == "__main__":
    main()

