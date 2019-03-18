import Chessboard as chess
import DFS as dfs
import HeuristicDFS as hdfs

## Test of a class Chessboard
# grid = (5,5)
# pos_knight = (0,3)
# chessboard = chess.Chessboard(grid, knight = pos_knight)

# print("Grid", chessboard.get_grid(), "Knight", chessboard.get_knight())
# states = chessboard.possible_states()

# i = 0
# for state in states:
#     i += 1
#     print("State #%d" % i)
#     for l in state:
#         print(l)
    
# del(chessboard)
####

def test_DFS(clss, grid, pos_knight):
        chessboard = chess.Chessboard(grid, knight = pos_knight)
        algorithm = None
        if clss == hdfs.HeuristicDFS:
                algorithm = hdfs.HeuristicDFS(chessboard)
        if clss == dfs.DFS:
                algorithm = dfs.DFS(chessboard)
        if algorithm == None:
                print('Wrong class!')
                return

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

def test_all(clss, grid):
        total_time = 0
        for i in range(grid[0]):
                for j in range(grid[1]):
                        total_time += test_DFS(clss, grid, (i,j))
        print("Total time is ", total_time, " seconds.\n" +
                "Average time is ", total_time/36) 

# test_DFS(hdfs.HeuristicDFS, (50,50), (0,0)) # 2.8 seconds
# test_DFS(hdfs.HeuristicDFS, (75,75), (0,0)) # 16 seconds
# test_DFS(dfs.DFS, (6,6), (0,0))
# test_DFS(dfs.DFS, (6,6), (0,1))
# test_DFS(hdfs.HeuristicDFS, (6,6), (0,2))
# test_DFS(hdfs.HeuristicDFS, (6,6), (3,2))
# test_DFS(hdfs.HeuristicDFS, (5,5), (0,2))
# test_DFS(dfs.DFS, (3,3), (0,2))

test_all(dfs.DFS, (3,3))
test_all(hdfs.HeuristicDFS, (6,6))
test_all(dfs.DFS, (6,6))

# test_all(hdfs.HeuristicDFS, (5,5))
# test_all(dfs.DFS, (5,5))
