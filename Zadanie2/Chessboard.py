
class Chessboard:
    __state = None
    __knight = None     # (type: tuple) position of a knight
    __grid = None       # (type: tuple) square of a board
    __area = None       # type: int
    __default = (0, 0)

    def __init__(self, grid, knight = __default):
        self.__state = list()   # type: list of lists
        self.__grid = grid
        self.__area = grid[0] * grid[1]
        self.__knight = knight

        ## Initialize a state
        for i in range (grid[0]):
            self.__state.append(list())
            for j in range(grid[1]):
                self.__state[i].append(0)

        self.__state[self.__knight[0]][self.__knight[1]] = 1    # Place a knight on a board

    ## Returns a list of possible future states.
    ## In the end of each state will be coordinates of a knight.
    def possible_states(self):
        states = list()
        x = self.__knight[0]
        y = self.__knight[1]

        # Up, Right
        if (x - 2 > 0) and (y + 1 < self.__grid[1]) and (self.__state[x - 2][y + 1] == 0):
            new_state = self.__new_list(self.__state)
            new_state[x - 2][y + 1] = new_state[x][y] + 1 
            new_state.append((x - 2, y + 1))
            states.append(new_state)

        # Right, Up 
        if (x - 1 >= 0) and (y + 2 < self.__grid[1]) and (self.__state[x - 1][y + 2] == 0):
            new_state = self.__new_list(self.__state)
            new_state[x - 1][y + 2] = new_state[x][y] + 1 
            new_state.append((x - 1, y + 2))
            states.append(new_state)
        
        # Right, Down
        if (x + 1 < self.__grid[0]) and (y + 2 < self.__grid[1]) and (self.__state[x + 1][y + 2] == 0):
            new_state = self.__new_list(self.__state)
            new_state[x + 1][y + 2] = new_state[x][y] + 1 
            new_state.append((x + 1, y + 2))
            states.append(new_state)

        # Down, Right
        if (x + 2 < self.__grid[0]) and (y + 1 < self.__grid[1]) and (self.__state[x + 2][y + 1] == 0):
            new_state = self.__new_list(self.__state)
            new_state[x + 2][y + 1] = new_state[x][y] + 1 
            new_state.append((x + 2, y + 1))
            states.append(new_state)

        # Down, Left
        if (x + 2 < self.__grid[0]) and (y - 1 >= 0) and (self.__state[x + 2][y - 1] == 0):
            new_state = self.__new_list(self.__state)
            new_state[x + 2][y - 1] = new_state[x][y] + 1 
            new_state.append((x + 2, y - 1))
            states.append(new_state)

        # Left, Down
        if (x + 1 < self.__grid[0]) and (y - 2 >= 0) and (self.__state[x + 1][y - 2] == 0):
            new_state = self.__new_list(self.__state)
            new_state[x + 1][y - 2] = new_state[x][y] + 1 
            new_state.append((x + 1, y - 2))
            states.append(new_state)

        # Left, Up
        if (x - 1 >= 0) and (y - 2 >= 0 ) and (self.__state[x - 1][y - 2] == 0):
            new_state = self.__new_list(self.__state)
            new_state[x - 1][y - 2] = new_state[x][y] + 1 
            new_state.append((x - 1, y - 2))
            states.append(new_state)

        # Up, Left
        if (x - 2 >= 0) and (y - 1 >= 0) and (self.__state[x - 2][y - 1] == 0):
            new_state = self.__new_list(self.__state)
            new_state[x - 2][y - 1] = new_state[x][y] + 1 
            new_state.append((x - 2, y - 1))
            states.append(new_state)

        return states

    ## Creates copy of a list of lists and returns it.
    def __new_list(self, lst):
        new_list = list()
        for l in lst:
            new_list.append(list(l))
        return new_list

    def change_state(self, state, knight):
        self.__state = state
        self.__knight = knight
    
    def get_grid(self):
        return self.__grid

    def get_knight(self):
        return self.__knight

    def get_state(self):
        return self.__state

    def is_goal_state(self):
        if self.__state[self.__knight[0]][self.__knight[1]] ==  self.__area:
            return True
        else:
            return False
        
