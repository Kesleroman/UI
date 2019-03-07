import Chessboard as chess
import DFS as dfs

## Test of a class Chessboard
""" grid = (5,5)
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
    
del(chessboard) """

## Test of a DFS
grid = (8,8)
pos_knight = (0,0)
chessboard = chess.Chessboard(grid, knight = pos_knight)
algorithm = dfs.DFS(chessboard)

chessboard = algorithm.get_chessboard()
print(chessboard)

if algorithm.run() == False:
        print("Can't find the answer")
else:
        for line in chessboard.get_state():
                print(line)

del(chessboard,algorithm)