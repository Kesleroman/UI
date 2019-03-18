class Node:
    __state = None
    __knight = None

    def __init__(self, state, knight):
        self.__state = state
        self.__knight = knight
    
    def get_state(self):
        return self.__state

    def get_knight(self):
        return self.__knight
