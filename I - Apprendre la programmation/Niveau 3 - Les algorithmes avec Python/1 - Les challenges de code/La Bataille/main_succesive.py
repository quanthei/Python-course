import sys
import math


CARDS_RANKING = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A") # Tuple with cards ranking

def play_a_turn(card_player_1: str, card_player_2: str) -> int:
    """ FUNCTION RETURNS
    0 - BATTLE
    1 - P1 wins
    2 - P2 wins
    """ 
    card_p1 = list(card_player_1) # convert the card of the player into a list to get the facial value only
    card_p2 = list(card_player_2) # convert the card of the player into a list to get the facial value only
    
    if CARDS_RANKING.index(card_p1[0]) == CARDS_RANKING.index(card_p1[0]): # Battle
        return 0
    elif CARDS_RANKING.index(card_p2[0]) > CARDS_RANKING.index(card_p2[0]): # Player 1 wins over Player 2
        return 1
    # Player 2 wins over Player 1
    return 2

@staticmethod
def recompose_decks(deck_to_be_filled, deck_to_be_stripped, cards_player_1, cards_player_2):
    deck_to_be_filled.extend([cards_player_1, cards_player_2])
    deck_to_be_stripped.pop(0)
     
n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

while len(cardp_1) != 0 and len(cardp_2) != 0: # on continue de jouer tant que les joueurs ont des cartes
    turn_result = play_a_turn(cardp_1[0], cardp_2[0]) # Play a turn
    winning_deck = []
    losing_deck = []

    if turn_result == 0: 
        print("BATTLE")
    else:
        if turn_result == 1:
            winning_deck, losing_deck = cardp_1, cardp_2
        else:
            winning_deck, losing_deck = cardp_2, cardp_1
        
        print(f"{winning_deck[0]} is more powerful than {losing_deck[0]}")
        print(f"Player {turn_result} win the turn !")
        
        # Recompose the decks
        recompose_decks(winning_deck, losing_deck, cardp_1[0], cardp_2[0])

print("PLUS DE CARTE")
# print("PAT")