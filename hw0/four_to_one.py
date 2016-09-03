def primitive(pos):
    if pos == 0:
        return "L"
    else:
        return "U"

"""
Returns the starting position.
"""
def initial_position():
    return 4

"""
Subtracts pos and move.
"""
def do_moves(move, pos):
    return pos - move

"""
Returns a list of all possible moves that can be made
""" 
def gen_moves(pos):
    all_moves = []
    if pos > 1:
        return [1, 2]
    elif pos > 0:
        return [1]
    else:
        return all_moves