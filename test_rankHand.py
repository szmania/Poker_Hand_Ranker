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

def main():
    """
    Run brute-force test for rankHand giving 1000 random hand types.
    """

    setup_logger()

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

