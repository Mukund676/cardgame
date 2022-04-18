from cgi import test
from enum import Enum
from enum import IntEnum
from random import *
from numpy import full

full_deck = []
partial_deck = []
player_1_deck = []
player_2_deck = []

class Card(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

class Suit(Enum):
    SPADES = 'spades'
    CLUBS = 'clubs'
    HEARTS = 'hearts'
    DIAMONDS = 'diamonds'

class PlayingCard:
    def __init__(self, card_value,card_suit):
        self.card = card_value
        self.suit = card_suit

def create_deck():
    for suit in Suit:
        for card in Card:
            full_deck.append(PlayingCard(Card(card),Suit(suit)))
    return full_deck

def draw_card(deck):
    rand_card = randint(0,len(deck)-1)
    return deck.pop(rand_card)

create_deck()
partial_deck = list(full_deck)

def deal_war():
    while (len(partial_deck)>0):
        player_1_deck.append(draw_card(partial_deck))
        player_2_deck.append(draw_card(partial_deck))
    


deal_war()
player_1_score = 0
player_2_score = 0
for i in range(0, len(player_1_deck)):
    if (player_1_deck[i].card > player_2_deck[i].card):
        print('Player 1 wins the hand with: ', player_1_deck[i].card)
        print('Player 2 loses the hand with: ', player_2_deck[i].card)
        player_1_score+=1
    elif (player_1_deck[i].card < player_2_deck[i].card):
        print('Player 1 loses the hand with: ', player_1_deck[i].card)
        print('Player 2 wins the hand with: ', player_2_deck[i].card)
        player_2_score+=1
    else:
        print('WAR TIME POG')
    print('\n')

if (player_1_score>player_2_score):
    print('Player 1 wins by '+str(player_1_score-player_2_score)+ ' point(s).')
elif (player_1_score<player_2_score):
    print('Player 2 wins by '+str(player_2_score-player_1_score)+ ' point(s).')
else:
    print("It's somehow a draw idk how")
