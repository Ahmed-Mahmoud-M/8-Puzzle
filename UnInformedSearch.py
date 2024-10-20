
from State import State
import heapq




class UnInformedSearch:
    def __init__(self,initalstate:State):
        self.inital = initalstate


    def BFS_search(self):
        frontier = []
        frontier.append(self.inital) 
        explored = set()

        while frontier:
            state = frontier.pop(0)  
            

            if state.is_goalstate():
                #state.print_puzzle()
                return state

            explored.add(state)  

            for neighbor in state.get_neighbors():
                 
                if neighbor not in frontier and neighbor not in explored:
                    frontier.append(neighbor)  
                    explored.add(neighbor)

        return None

        


    def DFS_search(self):
        frontier = []
        frontier.append(self.inital) 
        explored = set()

        while frontier:
            state = frontier.pop()  
            

            if state.is_goalstate():
               # state.print_puzzle()
                return state

            explored.add(state)  

            for neighbor in state.get_neighbors():
                 
                if neighbor not in frontier and neighbor not in explored:
                    frontier.append(neighbor)  
                    


        return None

    
        




    
        