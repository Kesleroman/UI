class Node:
    __state = None
    __knight = None
    __prev = None     # A parent of this node.

    def __init__(self, state, knight, prev):
        self.__state = state
        self.__knight = knight
        self.__prev = prev   
    
    def get_state(self):
        return self.__state

    def get_knight(self):
        return self.__knight
