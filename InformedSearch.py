from PriorityQueue import PriorityQueue



class InformedSearch:
    def __init__(self, initialState):
        self.initialState = initialState

    def Astar(self):
        frontier = PriorityQueue()
        frontier.insert(self.initialState)  
        explored = set()

        while not frontier.is_empty():  
            state = frontier.deleteMin() 
            explored.add(state)

            if state.is_goalstate(): 
                return state
            
            for neighbor in state.get_neighbors():
                if neighbor not in explored:
                    frontier.insert(neighbor)  
                elif neighbor in frontier.frontier:
                    frontier.decrease_key(neighbor)

        return None


                    