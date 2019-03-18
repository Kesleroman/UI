import Chessboard
import Node as node 

class Algorithm:
    __state = None      # Current state
    __chessboard = None
    spent_time = None

    def __init__(self, chessboard):
        self.__chessboard = chessboard
        self.__state = node.Node(chessboard.get_state(), chessboard.get_knight())

    def run(self):
        raise NotImplementedError

    def get_chessboard(self):
        return self.__chessboard
    
    def get_state(self):
        return self.__state
    