
class Chessboard:
    __state = None      # (type: list of lists)
    __knight = None     # (type: tuple) position of a knight
    __grid = None       # (type: tuple) square of a board
    __area = None       # type: int
    __default = (0, 0)  # Default position of a knight

    def __init__(self, grid, knight = __default):
        self.__state = list()   
        self.__grid = grid
        self.__area = grid[0] * grid[1]
        self.__knight = knight

        ## Initialize a state
        for i in range (grid[0]):
            self.__state.append(list())
            for j in range(grid[1]):
                self.__state[i].append(0)

        self.__state[self.__knight[0]][self.__knight[1]] = 1    # Place a knight on a board

    def __next_state(self, horisontal, vertical):
        x = self.__knight[0] + horisontal
        y = self.__knight[1] + vertical

        if  (x >= 0) and (x < self.__grid[0]) and (y >= 0) and (y < self.__grid[1]) and (self.__state[x][y] == 0):
            new_state = self.__new_list(self.__state)                             # copy a state of the chessboard 
            new_state[x][y] = new_state[self.__knight[0]][self.__knight[1]] + 1   # increments a number of a turn
            new_state.append((x, y))                                              # appends a new position of a knight
            return new_state   
        
        return None    

    ## Returns a list of possible future states.
    ## In the end of each state will be coordinates of a knight.
    def possible_states(self):
        states = list()
        x = self.__knight[0]
        y = self.__knight[1]

        # Up, Right
        new_state = self.__next_state(-2, 1)
        if new_state != None:
            states.append(new_state)                     

        # Right, Up 
        new_state = self.__next_state(-1, 2)
        if new_state != None:
            states.append(new_state)                     
        
        # Right, Down
        new_state = self.__next_state(1, 2)
        if new_state != None:
            states.append(new_state)                     

        # Down, Right
        new_state = self.__next_state(2, 1)
        if new_state != None:
            states.append(new_state)                     

        # Down, Left
        new_state = self.__next_state(2, -1)
        if new_state != None:
            states.append(new_state)          

        # Left, Down
        new_state = self.__next_state(1, -2)
        if new_state != None:
            states.append(new_state)

        # Left, Up
        new_state = self.__next_state(-1, -2)
        if new_state != None:
            states.append(new_state)

        # Up, Left
        new_state = self.__next_state(-2, -1)
        if new_state != None:
            states.append(new_state)

        return states

    ## Creates a copy of a list of lists and returns it.
    def __new_list(self, lst):
        new_list = list()
        for l in lst:
            new_list.append(list(l))
        return new_list

    def change_state(self, state, knight):
        self.__state = state
        self.__knight = knight

    def is_goal_state(self):
        if self.__state[self.__knight[0]][self.__knight[1]] ==  self.__area:    # if a number of a turn is equal to an area of the chessboard.
            return True
        else:
            return False
        
    def get_grid(self):
        return self.__grid

    def get_knight(self):
        return self.__knight

    def get_state(self):
        return self.__state
