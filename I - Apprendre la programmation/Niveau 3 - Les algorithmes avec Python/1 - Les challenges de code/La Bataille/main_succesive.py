import sys
import math

""" FUNCTIONS RETURNS
0 - BATTLE
1 - P1 wins
2 - P2 wins"""
def highest_card(card_player_1: str, card_player_2: str) -> int:

    # On define un tuple qui vient stocker le card ranking
    cards_ranking = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

    if cards_ranking.index(card_player_1) == cards_ranking.index(card_player_2): # Battle
        print("BATTLE")
    elif cards_ranking.index(card_player_1) > cards_ranking.index(card_player_2): # Player 1 wins over Player 2
        print("BATTLE")
        return "P1"
        return # Player 2 wins over Player 1
        return "P1"


n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("PAT")
