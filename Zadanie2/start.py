import Chessboard as chess

## Test of a class Chessboard
grid = (5,5)
pos_knight = (0,3)
chessboard = chess.Chessboard(grid, knight = pos_knight)

print("Grid", chessboard.get_grid(), "Knight", chessboard.get_knight())
states = chessboard.possible_states()

i = 0
for state in states:
    i += 1
    print("State #%d" % i)
    for l in state:
        print(l)
    
del(chessboard)

