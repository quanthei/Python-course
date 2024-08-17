import sys

CARDS_RANKING = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A") # Tuple with cards ranking

def play_a_turn(card_p1: str, card_p2: str) -> int:
    """ FUNCTION RETURNS
    0 - BATTLE
    1 - P1 wins
    2 - P2 wins
    """
    card_value_p1 = card_p1[0] # get the facial value only
    card_value_p2 = card_p2[0] # get the facial value only

    if CARDS_RANKING.index(card_value_p1) == CARDS_RANKING.index(card_value_p2): # Battle
        return 0
    elif CARDS_RANKING.index(card_value_p1) > CARDS_RANKING.index(card_value_p2): # Player 1 wins over Player 2
        return 1
    # Player 2 wins over Player 1
    return 2

def play_battle(deck_p1, deck_p2):
    draws_p1 = [deck_p1.pop(0) for _ in range(3)]
    draws_p2 = [deck_p2.pop(0) for _ in range(3)]
    return draws_p1, draws_p2

# Get the decks
n = int(input())  # the number of cards for player 1
deck_player_1 = [input() for _ in range(n)] # the n cards of player 1
m = int(input())  # the number of cards for player 2
deck_player_2 = [input() for _ in range(m)]  # the m cards of player 2

# Start to play
turns = 0
while len(deck_player_1) > 0 and len(deck_player_2) > 0: # while both players keep having at least one card we keep playing
    turns += 1
    card_p1 = deck_player_1.pop(0)
    card_p2 = deck_player_2.pop(0)
    turn_result = play_a_turn(card_p1, card_p2)

    if turn_result == 0:  # Battle
        if len(deck_player_1) < 3 or len(deck_player_2) < 3:
            print("PAT")
            break
        draws_p1, draws_p2 = play_battle(deck_player_1, deck_player_2)
        card_p1 = deck_player_1.pop(0)
        card_p2 = deck_player_2.pop(0)
        turn_result = play_a_turn(card_p1, card_p2)
        if turn_result == 1:
            deck_player_1.extend([card_p1, card_p2] + draws_p1 + draws_p2)
        else:
            deck_player_2.extend([card_p1, card_p2] + draws_p1 + draws_p2)
    else:
        if turn_result == 1:
            deck_player_1.extend([card_p1, card_p2])
        else:
            deck_player_2.extend([card_p1, card_p2])

if len(deck_player_1) == 0:
    print(f"2 {turns}")
elif len(deck_player_2) == 0:
    print(f"1 {turns}")
