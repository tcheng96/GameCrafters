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
    if pos > 1:
        return [1, 2]
    else
        return [1]

"""
Solver for 4-to-1 Game
"""
def solver(pos, gameStates):
    result

"""
Determine winner.
"""
def traverse_game_tree(pos):
    if primitive(pos) != "U":
        return primitive(pos)
    curr = "L"
    all_moves = four.gen_moves(pos)
    for move in all_moves:
        after_moves = four.do_moves(move, pos)
        result = traverse_game_tree(after_moves)
        if result == four.LOSE:
            curr = four.WIN
    return curr