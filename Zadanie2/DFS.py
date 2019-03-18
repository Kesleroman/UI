import Algorithm as alg
import Node as node
import time

class DFS(alg.Algorithm):
    __front = None      # A front of states
    __dic = None        # A dictionary for printed time

    def __init__(self, chessboard):
        super().__init__(chessboard)
        self.__dic = dict()
        self.__front = list()
        self.__generate_children()
    
    def run(self):
        start_time = time.time()
        while True:
            try:
                child = self.__front.pop(0)
            except:
                self.spent_time = time.time() - start_time
                return False

            self.get_chessboard().change_state(child.get_state(), child.get_knight())
            if self.get_chessboard().is_goal_state() == True:
                self.spent_time = time.time() - start_time
                print('%f seconds spent' % self.spent_time)
                return self.get_chessboard()

            self.__generate_children()
            curr_time = int(time.time() - start_time)

            ## Print spent time every five seconds
            if curr_time % 5 == 0:
                if self.__dic.get(curr_time, 0) == 0:     # if current time from the start hasn't been printed before 
                    self.__dic[curr_time] = 1
                    print("%d seconds from start." % curr_time)

            ## If search of the solution is too long.
            limit = 16  # seconds 
            if curr_time > limit: 
                self.spent_time = limit 
                return False
    
    def __generate_children(self):
        pos_states = self.get_chessboard().possible_states()
        for state in pos_states:
            knight = state.pop()
            new_node = node.Node(state, knight)
            self.__front.insert(0, new_node)
        
