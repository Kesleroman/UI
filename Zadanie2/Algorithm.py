import Chessboard

class Algorithm:
    __chessboard = None

    def __init__(self, chessboard):
        self.__chessboard = chessboard

    def run(self):
        raise NotImplementedError

    def get_chessboard(self):
        return self.__chessboard    

    