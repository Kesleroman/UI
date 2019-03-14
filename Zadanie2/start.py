import Chessboard as chess
import DFS as dfs
import HeuristicDFS as hdfs

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

def test_DFS(grid, pos_knight):
        chessboard = chess.Chessboard(grid, knight = pos_knight)
        algorithm = hdfs.HeuristicDFS(chessboard)

        chessboard = algorithm.get_chessboard()
        print('')

        if algorithm.run() == False:
                print("For the grid", grid, "with the start position", pos_knight, "couldn't find the answer.")
        else:
                for line in chessboard.get_state():
                        print(line)

        spent_time = algorithm.spent_time
        del(chessboard,algorithm)
        return spent_time

# test_DFS((50,50), (0,0)) # 2.8 seconds
# test_DFS((75,75), (0,0)) # 16 seconds
# test_DFS((6,6), (0,0))
# test_DFS((6,6), (0,1))
# test_DFS((6,6), (0,2))
# test_DFS((6,6), (3,2))
# test_DFS((5,5), (0,2))
# test_DFS((3,3), (0,2))

# total_time = 0
# for i in range(6):
#         for j in range(6):
#                 total_time += test_DFS((6,6), (i,j))
# print("Total time is ", total_time, " seconds.\n" +
#         "Average time is ", total_time/36) 

                