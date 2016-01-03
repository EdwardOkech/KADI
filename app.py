from settings import messages
import os
import random
import time
import  pygame

"""
KADI is a card game played by  one person vs a computer opponent
the game is quite simple, the first person to finish his/her card-hand wins
"""
# global variables


# CENTER_CARD is the card that will always be at the center of the table
CENTER_CARD = []

# DECK is the game deck of cards
# DECK = []

# PLAYERS is a list of the players in the game
PLAYERS = []

# suits is a suit of cards
# SUITS = 'SDHC'


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '{0}{1}'.format(self.suit, self.rank)

    @staticmethod
    def make_cards(deck):
        for suit in 'SDHC':
            for rank in range(1, 14):
                deck.append(suit + str(rank))
                list(deck)
                yield Card(suit, rank)


class Human(Card):
    """
    Creates the human player attributes
    """
    def __init__(self, ):


class Computer(Card):
    """
    computer objects
    """
    def __init__(self, comp, comp_hand=None):
        super(Computer, self).__init__(deck=None)
        if comp_hand is None:
            comp_hand = []
        self.comp = comp
        self.comp_hand = comp_hand

    def __str__(self):
        return '{0} your cards are : {1}'.format(self.comp, self.comp_hand)

    def make_hand(self):
        self.comp_hand.append(self.deck[-4:])


# class PlayingCard(Human, Computer, Card):
#     def __init__(self):
#
#
#     def human_playing_card(self):
#         return self.player_hand.remove(self.deck)
#
#     def comp_playing_card(self):
#         pass

# class ArtificialIntelligence(Card,Computer):
#     """
#     Game A.I used by the computer to play
#     """
#     def __init__(self, comp, move):
#         super(ArtificialIntelligence, self).__init__(comp)
#         self.move = move
#
#
#     def check_first_payer(self):
#         """
#         this method helps
#         """


class Score(object):
    def __init__(self, high_score, score=0):
        self.high_score = high_score
        self.score = score

    def get_score(self):
        return self.score

    def set_score(self):
        self.score = self.update_score()

    def update_score(self):
        self.score += 5
        return self.score

    def get_high_score(self):
        return list(self.high_score)

    @classmethod
    def set_high_scores(cls, scores):
        for high_score in sorted(scores[-3:]):
            yield cls(high_score)


def main():
    # Initializes the game
    Human.name = raw_input('Enter your name')
    PLAYERS.append(Human.name)
    # PLAYERS.append(Computer.comp)


    # # first player to play
    # first_player = random.choice(PLAYERS)
    #
    # # getting the second player logic
    # fi = 0 # obvious first index in the players list
    # fpi = PLAYERS.index(first_player) # index of the player playing first
    # if fpi == fi: # if the first_player's index equals the first index of PLAYERS list
    #     fi += 1 # then we increament fi by 1
    #     second_player = PLAYERS[fi]  # since they are only 2 players it makes sence to give the payer 2 index fi
    #
    #
    # print 'Congratulation, ' + first_player + 'your will have the first turn in this game'

    # shuffles the card deck
    # Card.make_cards()

    while len(Card.deck) > 0 or len(Card.deck) <= 52:
        messages("may the game begin their is no cheating" % (PLAYERS,))
        # deals to the human
        Human.make_hand()
        # deals to the computer
        Computer.make_hand()
        # places the starting card in the midde of the table
        CENTER_CARD.append(Card.deck[-1:])

        print CENTER_CARD
        print Human.player_hand
        print Human.name + ' it is your turn to play'
        human_playin_card = raw_input('play card:')
        for equal_card in (Human.player_hand , Computer.comp_hand):
            if human_playin_card is equal_card or human_playin_card[0] is equal_card[0]:
                CENTER_CARD.append(Human.player_hand.remove(human_playin_card))
            # if (human_playin_card[-1] or human_playin_card[-1]) in  :


# call the "main" function if running this script

if __name__ == '__main__':
    main()










