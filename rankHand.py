###
# Created by Curtis Szmania
# Date: 06/10/17
# Comment: comScore coding assessment
###

__author__ = 'szmania'

from argparse import ArgumentParser
from logging import DEBUG, getLogger, FileHandler, Formatter, StreamHandler
from sys import stdout


LOG = 'rankHand.log'


class RankHand(object):
    def __init__(self, logLevel='DEBUG', **kwargs):
        self.__logLevel = logLevel

        # self._setup_logger(logFile=LOG)
        self._assign_attributes(**kwargs)

        self.__hand = Hand(card1=kwargs['card1'], card2=kwargs['card2'],
                           card3=kwargs['card3'], card4=kwargs['card4'],
                           card5=kwargs['card5'], logLevel=logLevel)

    # def __del__(self):
    #
    #     self._tear_down_logger()

    @property
    def hand(self):
        """
        hand attribtue.

        :return: Return __hand attribute
        """
        logger = getLogger('RankdHand.hand')
        logger.setLevel(self.__logLevel)

        return self.__hand

    def _assign_attributes(self, **kwargs):
        """
        Assign argumetns to class attributes.

        :param kwargs:  Dictionary of arguments.
        :type kwargs: Dictionary

        :return:
        """

        logger = getLogger('RankHand._assign_attributes')
        logger.setLevel(self.__logLevel)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_rank(self):
        """
        Return rank of hand as integer.

        :return: Integer signifying rank of hand in relation to other possible hands.
        """

        logger = getLogger('RankHand.getRank')
        logger.setLevel(self.__logLevel)

        rank = None

        if self.__hand.royal_flush:
            print('Hand is Royal Flush.')
            rank = 1
        elif self.__hand.straight_flush:
            print('Hand is Straight Flush.')
            rank = 2
        elif self.__hand.four_of_a_kind:
            print('Hand is Four of a Kind.')
            rank = 3
        elif self.__hand.full_house:
            print('Hand is Full House.')
            rank = 4
        elif self.__hand.flush:
            print('Hand is Flush.')
            rank = 5
        elif self.__hand.straight:
            print('Hand is Straight.')
            rank = 6
        elif self.__hand.three_of_a_kind:
            print('Hand is Three of a Kind.')
            rank = 7
        elif self.__hand.two_pairs:
            print('Hand is Two Pairs.')
            rank = 8
        elif self.__hand.two_of_a_kind:
            print('Hand is Pair')
            rank = 9
        elif self.__hand.highCard:
            print('Hand is High Card.')
            rank = 10

        if rank:
            print('Rank of hand is %s.' % str(rank))
            print('Hand: %s' % self.__hand.str)
            return rank
        else:
            raise CantRank('Can NOT rank hand: "%s"' % self.__hand.str)

class CantRank(Exception):
    pass

class Hand(object):

    def __init__(self, card1, card2, card3, card4, card5, logLevel='DEBUG'):
        """
        Hand class to handle every hand.

        :param card1: Card as tuple in the form ("10", "S") = 10 of spades, ("J", "D") =  Jack of Diamonds, etc... (See Card class for more details)
        :type card1: Tuple.
        :param card2: Card as tuple in the form ("10", "S") = 10 of spades, ("J", "D") =  Jack of Diamonds, etc... (See Card class for more details)
        :type card2: Tuple.
        :param card3: Card as tuple in the form ("10", "S") = 10 of spades, ("J", "D") =  Jack of Diamonds, etc... (See Card class for more details)
        :type card3: Tuple.
        :param card4: Card as tuple in the form ("10", "S") = 10 of spades, ("J", "D") =  Jack of Diamonds, etc... (See Card class for more details)
        :type card4: Tuple.
        :param card5: Card as tuple in the form ("10", "S") = 10 of spades, ("J", "D") =  Jack of Diamonds, etc... (See Card class for more details)
        :type card5: Tuple.
        """

        self.__card1 = Card(card1[0], card1[1], logLevel=logLevel)
        self.__card2 = Card(card2[0], card2[1], logLevel=logLevel)
        self.__card3 = Card(card3[0], card3[1], logLevel=logLevel)
        self.__card4 = Card(card4[0], card4[1], logLevel=logLevel)
        self.__card5 = Card(card5[0], card5[1], logLevel=logLevel)

        self.__logLevel = logLevel

        logger = getLogger('Hand.__init__')
        logger.setLevel(self.__logLevel)

        self.__hand = [self.__card1, self.__card2, self.__card3, self.__card4, self.__card5]

        self.__cardCount = {}
        self.__flush = False
        self.__four_of_a_kind = False
        self.__full_house = False
        self.__highCard = None
        self.__royal_flush = False
        self.__straight = False
        self.__straight_flush = False
        self.__two_pairs = False
        self.__two_of_a_kind = False
        self.__three_of_a_kind = False

        self.__str = self._form_hand_string()

        self.__highCard = self._get_highest_card()
        self.__straight = self._is_straight()
        self.__flush = self._is_flush()
        self.__royal_flush = self._is_royal_flush()
        self.__straight_flush = self._is_straight_flush()
        self.__cardCount = self._count_cards()
        self.__two_of_a_kind = self._is_two_of_a_kind()
        self.__two_pairs = self._is_two_pairs()
        self.__three_of_a_kind = self._is_three_of_a_kind()
        self.__full_house = self._is_full_house()
        self.__four_of_a_kind = self._is_four_of_a_kind()

        if self._no_duplicates():
            logger.debug(' Hand created with cards: "%s, %s, %s, %s, %s"' % (card1, card2, card3, card4, card5))

    @property
    def cardCount(self):
        """
        cardCount attribtue.

        :return: Return __cardCount attribute
        """
        logger = getLogger('Hand.cardCount')
        logger.setLevel(self.__logLevel)

        return self.__cardCount

    @property
    def flush(self):
        """
        flush attribtue.

        :return: Return __flush attribute
        """
        logger = getLogger('Hand.flush')
        logger.setLevel(self.__logLevel)

        return self.__flush

    @property
    def four_of_a_kind(self):
        """
        four_of_a_kind attribtue.

        :return: Return __four_of_a_kind attribute
        """
        logger = getLogger('Hand.four_of_a_kind')
        logger.setLevel(self.__logLevel)

        return self.__four_of_a_kind

    @property
    def full_house(self):
        """
        full_house attribtue.

        :return: Return __full_house attribute
        """
        logger = getLogger('Hand.full_house')
        logger.setLevel(self.__logLevel)

        return self.__full_house

    @property
    def hand(self):
        """
        hand attribtue.

        :return: Return __hand attribute
        """
        logger = getLogger('Hand.hand')
        logger.setLevel(self.__logLevel)

        return self.__hand

    @property
    def highCard(self):
        """
        highCard attribtue.

        :return: Return __highCard attribute
        """
        logger = getLogger('Hand.highCard')
        logger.setLevel(self.__logLevel)

        return self.__highCard

    @property
    def royal_flush(self):
        """
        royal_flush attribtue.

        :return: Return __royal_flush attribute
        """
        logger = getLogger('Hand.royal_flush')
        logger.setLevel(self.__logLevel)

        return self.__royal_flush

    @property
    def straight(self):
        """
        straight attribtue.

        :return: Return __straight attribute
        """
        logger = getLogger('Hand.straight')
        logger.setLevel(self.__logLevel)

        return self.__straight

    @property
    def straight_flush(self):
        """
        straight_flush attribtue.

        :return: Return __straight_flush attribute
        """
        logger = getLogger('Hand.straight_flush')
        logger.setLevel(self.__logLevel)

        return self.__straight_flush

    @property
    def str(self):
        """
        str attribtue for Hand. Hand in string format.

        :return: Return __str attribute, as string.
        """
        logger = getLogger('Hand.str')
        logger.setLevel(self.__logLevel)

        return self.__str

    @property
    def three_of_a_kind(self):
        """
        three_of_a_kind attribtue for Hand.

        :return: Return __three_of_a_kind attribute, as string.
        """
        logger = getLogger('Hand.three_of_a_kind')
        logger.setLevel(self.__logLevel)

        return self.__three_of_a_kind

    @property
    def two_of_a_kind(self):
        """
        two_of_a_kind attribtue for Hand.

        :return: Return __two_of_a_kind attribute, as string.
        """
        logger = getLogger('Hand.tow_of_a_kind')
        logger.setLevel(self.__logLevel)

        return self.__two_of_a_kind

    @property
    def two_pairs(self):
        """
        two_pairs attribtue.

        :return: Return __two_pairs attribute
        """
        logger = getLogger('Hand.two_pairs')
        logger.setLevel(self.__logLevel)

        return self.__two_pairs

    def _count_cards(self):
        """
        Counts card types in hand.

        :return:
        """

        logger = getLogger('Hand._count_cards')
        logger.setLevel(self.__logLevel)

        types = Card.get_types()
        cardCount = {}
        totalCount = 0
        for cardType in types:
            count = 0
            for card in self.__hand:
                if card.type == cardType:
                    count = count + 1

            if count > 0:
                cardCount[cardType] = count
                totalCount = totalCount + count
                if totalCount >= 5: break
        return cardCount

    def _get_highest_card(self):
        """
        Get hand highest card.

        :return: Return highest card.
        """

        logger = getLogger('Hand._get_highest_card')
        logger.setLevel(self.__logLevel)

        sortedHand = Hand.sort_hand(hand=self.__hand)

        return sortedHand[-1].type

    def _is_flush(self):
        """
        Determines if hand is a flush.

        :return: Boolean of true if a flush.
        """

        logger = getLogger('Hand._is_flush')
        logger.setLevel(self.__logLevel)

        for card1 in self.__hand:
            for card2 in self.__hand:
                if card1.suite != card2.suite:
                    logger.debug(' Hand is NOT a flush: "%s"' % self.__str)
                    return False

        logger.debug(' Hand is a flush: "%s"' % self.__str)
        return True

    def _is_four_of_a_kind(self):
        """
        Determines if hand is four of a kind.

        :return: Boolean of true if is four of a kind.
        """

        logger = getLogger('Hand._is_four_of_a_kind')
        logger.setLevel(self.__logLevel)

        for count in self.__cardCount.values():
            if count == 4:
                logger.debug(' Hand is Four of a Kind: "%s"' % self.__str)
                return True

        logger.debug(' Hand is NOT Four of a Kind: "%s"' % self.__str)
        return False

    def _is_full_house(self):
        """
        Determines if hand is a full house.

        :return: Boolean of true if is a full house.
        """

        logger = getLogger('Hand._is_full_house')
        logger.setLevel(self.__logLevel)

        if self.__two_of_a_kind and self.__three_of_a_kind:
                logger.debug(' Hand is a Full House: "%s"' % self.__str)
                return True

        logger.debug(' Hand is NOT a Full House: "%s"' % self.__str)
        return False

    def _is_royal_flush(self):
        """
        Determines if hand is royal flush

        :return: Boolean of true if royal flush.
        """

        logger = getLogger('Hand._is_royal_flush')
        logger.setLevel(self.__logLevel)

        if self.__straight and self.__flush and self.__highCard == 'A':
            logger.debug(' Hand is Royal Flush: "%s"' % self.__str)
            return True
        else:
            logger.debug(' Hand is NOT Royal Flush: "%s"' % self.__str)
            return False

    def _is_straight(self):
        """
        Determines if hand is a straight.

        :return: Boolean of true if a straight.
        """

        logger = getLogger('Hand._is_straight')
        logger.setLevel(self.__logLevel)

        sortedHand = Hand.sort_hand(self.__hand)

        sortedTypes = []
        for card in sortedHand:
            sortedTypes.append(card.type)

        types = Card.get_types()
        if ''.join(map(str, sortedTypes)) in ''.join(map(str, types)):
            logger.debug(' Hand is a straight: "%s"' % self.__str)
            return True
        else:
            logger.debug(' Hand is NOT a straight: "%s"' % self.__str)
            return False

    def _is_straight_flush(self):
        """
        Determines if hand is a straight flush.

        :return: Boolean of true if hand is a stragith flush.
        """

        logger = getLogger('Hand._is_straight_flush')
        logger.setLevel(self.__logLevel)

        if self.__straight and self.__flush:
            logger.debug(' Hand is Straight Flush: "%s"' % self.__str)
            return True
        else:
            logger.debug(' Hand is NOT Straight Flush: "%s"' % self.__str)
            return False

    def _is_two_pairs(self):
        """
        Determines if hand is two pairs.

        :return: Boolean of true if is two pairs.
        """

        logger = getLogger('RankHand._is_two_pairs')
        logger.setLevel(self.__logLevel)

        firstPair = False
        secondPair = False

        for count in self.__cardCount.values():
            if count == 2 and not firstPair:
                firstPair = True
            elif count == 2 and firstPair:
                secondPair = True

            if firstPair and secondPair:
                logger.debug(' Hand has Two Pairs: "%s"' % self.__str)
                return True

        logger.debug(' Hand does NOT have Two Pairs: "%s"' % self.__str)
        return False

    def _is_three_of_a_kind(self):
        """
        Determines if hand is a three of a kind.

        :return: Boolean of true if is a three of a kind.
        """

        logger = getLogger('Hand._is_three_of_a_kind')
        logger.setLevel(self.__logLevel)

        for count in self.cardCount.values():
            if count == 3:
                logger.debug(' Hand is a Three-of-a-Kind: "%s"' % self.str)
                return True

        logger.debug(' Hand is NOT a Three-of-a-Kind: "%s"' % self.str)
        return False

    def _is_two_of_a_kind(self):
        """
        Determines if hand is a two of a kind.

        :return: Boolean of true if is a two of a kind.
        """

        logger = getLogger('Hand._is_two_of_a_kind')
        logger.setLevel(self.__logLevel)

        for count in self.cardCount.values():
            if count == 2:
                logger.debug(' Hand is a Two-of-a-Kind: "%s"' % self.str)
                return True

        logger.debug(' Hand is NOT a Two-of-a-Kind: "%s"' % self.str)
        return False

    def _form_hand_string(self):
        """
        Form string representation of hand.

        :return: String representation of hand.
        """

        logger = getLogger('Hand._form_hand_string')
        logger.setLevel(self.__logLevel)

        cardStr = ''
        for card in self.__hand:
            if cardStr != '':
                cardStr = cardStr + ' - ' + card.str
            else:
                cardStr = card.str
        return cardStr

    def _no_duplicates(self):
        """
        Sees if hand has any duplicate cards, which would violate one deck rule.

        :return: Boolean of whether duplicate cards or not.
        """

        logger = getLogger('Hand._no_duplicate')
        logger.setLevel(self.__logLevel)

        for i in range(len(self.__hand)):
            card1 = self.__hand[i]
            for j in range(len(self.__hand)):
                card2 = self.__hand[j]
                if Hand.same_suite(card1=card1,card2=card2, logLevel=self.__logLevel) and Hand.same_type(card1=card1,card2=card2, logLevel=self.__logLevel) and i != j:
                    raise DuplicateCard('Given hand has duplicate cards: %s' % (self.__str))

        return True

    @staticmethod
    def sort_hand(hand, logLevel='DEBUG'):
        """
        Sort hand.

        :param hand: Hand object to sort.
        :type hand: Hand object.
        :param logLevel: Logging level. ie:  "DEBUG", "INFO", etc...
        :type logLevel: String.

        :return: Sorted Hand object.
        """

        logger = getLogger('Hand.sort_hand')
        logger.setLevel(logLevel)

        types = Card.get_types()

        sortedHand = []
        for cardType in types:
            for card in hand:
                if card.type == cardType:
                    sortedHand.append(card)
        return sortedHand

    @staticmethod
    def same_suite(card1, card2, logLevel='DEBUG'):
        """
        Compares two cards and returns if boolean of whether same suite or not.

        :param card1: First card object.
        :type card1: Card object.
        :param card2: Second card object.
        :type card2: Card object.
        :param logLevel: Logging level. ie:  "DEBUG", "INFO", etc...
        :type logLevel: String.

        :return: Boolean of whether card1 and card2 of the same suite.
        """

        logger = getLogger('Hand.same_suite')
        logger.setLevel(logLevel)

        if card1._Card__suite == card2._Card__suite:
            logger.debug(' Card "%s" and Card "%s" are same suite.' %(card1._Card__suite, card2._Card__suite))
            return True
        else:
            logger.debug(' Card "%s" and Card "%s" are NOT same suite.' % (card1._Card__suite, card2._Card__suite))
            return False

    @staticmethod
    def same_type(card1, card2, logLevel='DEBUG'):
        """
        Compares two cards and returns if boolean of whether same type or not.

        :param card1: First card object.
        :type card1: Card object.
        :param card2: Second card object.
        :type card2: Card object.
        :param logLevel: Logging level. ie:  "DEBUG", "INFO", etc...
        :type logLevel: String.

        :return: Boolean of whether card1 and card2 of the same type.
        """

        logger = getLogger('Hand.same_type')
        logger.setLevel(logLevel)

        if card1._Card__type == card2._Card__type:
            logger.debug(' Card "%s" and Card "%s" are same type.' % (card1._Card__type, card2._Card__type))
            return True
        else:
            logger.debug(' Card "%s" and Card "%s" are NOT same type.' % (card1._Card__type, card2._Card__type))
            return False

class DuplicateCard(Exception):
    pass

class Card(object):

    def __init__(self, cardType, suite, logLevel='DEBUG'):
        """
        Card class to handle every card.

        :param cardType: Type of card.
            "A": Ace
            "K": King
            "Q": Queen
            "J": Joker
            "10": 10
            "9": 9
            etc...
            "2": 2
        :type cardType: String.
        :param suite: Suite of card.
            "C": Clubs
            "D": Diamonds
            "H": Hearts
            "S": Spades
        :type suite: String.
        :param logLevel: Logging level. ie:  "DEBUG", "INFO", etc...
        :type logLevel: String.
        """

        self.__logLevel = logLevel

        logger = getLogger('Card.__init__')
        logger.setLevel(self.__logLevel)

        self.__str = cardType + ',' + suite

        if self._is_type(cardType) and self._is_suite(suite):
            logger.debug(' Card created: "%s, %s"' % (cardType, suite))

    @property
    def type(self):
        """
        type attribtue.

        :return: Return __type attribute
        """
        logger = getLogger('Card.type')
        logger.setLevel(self.__logLevel)

        return self.__type

    @property
    def str(self):
        """
        str attribtue. Card in string format.

        :return: Return __str attribute, as string.
        """
        logger = getLogger('Card.str')
        logger.setLevel(self.__logLevel)

        return self.__str

    @property
    def suite(self):
        """
        suite attribtue.

        :return: Return __suite attribute
        """
        logger = getLogger('Card.suite')
        logger.setLevel(self.__logLevel)

        return self.__suite

    def _is_type(self, value):
        """
        Checks if given value is a card type.

        :param value: Type of card, ie: 'A' = Aces, etc...
        :type value: String.

        :return: Boolean of whether value is a valid card type.
        """
        logger = getLogger('Card._is_type')
        logger.setLevel(self.__logLevel)

        types = Card.get_types()
        if value in types:
            self.__type = value
            return True
        else:
            raise NotType('Given value "%s" is not a type! "%s"' % (value, types))

    def _is_suite(self, value):
        """
        Checks if given value is a card suite.

        :param value: Suite of card, ie: 'C' = Clubs, etc...
        :type value: String.

        :return: Boolean of whether value is a valid suite type.
        """
        logger = getLogger('Card._is_suite')
        logger.setLevel(self.__logLevel)

        suites = Card.get_suites()
        if value in suites:
            self.__suite = value
            return True
        else:
            raise NotSuite('Given value "%s" is not a suite! "%s"' % (value, suites))

    @staticmethod
    def get_types(logLevel='DEBUG'):
        """
        Return card types.

        :param logLevel: Logging level. ie:  "DEBUG", "INFO", etc...
        :type logLevel: String.

        :return: Return list of card types. ie: 'A' = Ace, '4' = 4, etc...
        """
        logger = getLogger('Card.get_types')
        logger.setLevel(logLevel)

        types = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return types

    @staticmethod
    def get_suites(logLevel='DEBUG'):
        """
        Return card suites.

        :param logLevel: Logging level. ie:  "DEBUG", "INFO", etc...
        :type logLevel: String.

        :return: Return list of card suites. ie: 'S' = Spades, 'D' = Diamonds, etc...
        """
        logger = getLogger('Card.get_suites')
        logger.setLevel(logLevel)

        suites = ['C','D','H','S']
        return suites

class NotSuite(Exception):
    pass

class NotType(Exception):
    pass


def get_args():
    """
    Get arguments from command line, and returns them as dictionary.

    :return: Dictionary of arguments.
    :type: Dictionary.
    """

    parser = ArgumentParser(description='Give rank of poker hand given five sets of tuples representing five cards.')

    parser.add_argument('-c1', '--card1', dest='card1', type=lambda x: x.split(','), required=True,
                        help='Card 1 given as tuple. ie: "2", "C" or "3", "S", etc...')

    parser.add_argument('-c2', '--card2', dest='card2', type=lambda x: x.split(','), required=True,
                        help='Card 2 given as tuple. ie: "2", "C" or "3", "S", etc...')

    parser.add_argument('-c3', '--card3', dest='card3', type=lambda x: x.split(','), required=True,
                        help='Card 3 given as tuple. ie: "2", "C" or "3", "S", etc...')

    parser.add_argument('-c4', '--card4', dest='card4', type=lambda x: x.split(','), required=True,
                        help='Card 4 given as tuple. ie: "2", "C" or "3", "S", etc...')

    parser.add_argument('-c5', '--card5', dest='card5', type=lambda x: x.split(','), required=True,
                        help='Card 5 given as tuple. ie: "2", "C" or "3", "S", etc...')

    parser.add_argument('--log', dest='logLevel', default='INFO',
                        help='Set logging level')

    args = parser.parse_args()
    return args.__dict__

def setup_logger(logFile=LOG, logLevel='DEBUG'):
        """
        Logger setup.

        :param logFile:  Log file path.
        :type logFile: string
        """

        root = getLogger()
        root.setLevel(DEBUG)

        handler = FileHandler(logFile)
        formatter = Formatter('%(levelname)s:%(name)s:%(message)s')

        # formatter = logging.Formatter(fmt='%(message)s', datefmt='')
        handler.setLevel(DEBUG)
        handler.setFormatter(formatter)

        ch = StreamHandler(stdout)
        ch.setLevel(logLevel)
        ch.setFormatter(formatter)

        root.addHandler(handler)
        root.addHandler(ch)

        logger = getLogger('RankHand._setup_logger')
        logger.setLevel(logLevel)
        logger.debug(' Logging to %s' % logFile)


def main():

    setup_logger(logFile=LOG, logLevel='DEBUG')

    # UNCOMMENT TO ALLOW COMMAND LINE ARGUMENTS
    kwargs = get_args()
    rankObj = RankHand(**kwargs)
    rank = rankObj.get_rank()


if __name__ == "__main__":
    main()

