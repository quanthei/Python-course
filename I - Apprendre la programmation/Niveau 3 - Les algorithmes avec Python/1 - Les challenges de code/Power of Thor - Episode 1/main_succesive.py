import sys
import math
import copy

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# Positions
LIGHTER_INITIAL_POSITION = (light_x, light_y)
thor_actual_position = [initial_tx,initial_ty]
thor_position_temp = [0,0]

# Turn
actual_turn = 0

def north_or_south(): # Y
    if LIGHTER_INITIAL_POSITION[1] == thor_actual_position[1]:
        return ""
    else:
        thor_position_temp[1] += 1
        if LIGHTER_INITIAL_POSITION[1] > thor_actual_position[1]:
            return "N"
    return "S"

def west_or_est(): # X
    if LIGHTER_INITIAL_POSITION[0] == thor_actual_position[0]:
        return ""
    else:
        thor_position_temp[0] += 1
        if LIGHTER_INITIAL_POSITION[0] > thor_actual_position[0]:
            return "E"
    return "W"

# game loop
while True:
    instructions = "" # clean des instructions

    actual_turn += 1
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    if actual_turn == 1: # First init
        thor_position_temp = copy.copy(thor_actual_position)

    # Definir north ou south via Y
    instructions += north_or_south()

    # Definir east ou west via X
    instructions += west_or_est()

    # New thor_actual_position
    thor_actual_position = copy.copy(thor_position_temp)
    
    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(instructions)