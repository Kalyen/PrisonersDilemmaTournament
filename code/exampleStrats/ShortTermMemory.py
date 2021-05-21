import random

# This strategy decides what to do based on the last 3 turns.

def strategy(history, memory):
    choice = None
    
    if history.shape[1] < 3: # The first 3 turns are random
        choice = random.randint(0, 1)
    elif gameLength >= 3: # Then we do the same action that the opponent did most the last 3 turns.
        if history[1,-1] + history[1,-2] + history[1,-3] >= 2:
            choice = 1
        else:
            choice = 0
            
    return choice, None
