import heapq
class PriorityQueue(object):
    def __init__(self):
        self.frontier = []

    def is_empty(self):
        return len(self.frontier) == 0

    def insert(self, state):
        heapq.heappush(self.frontier, state)

    def deleteMin(self):
        return heapq.heappop(self.frontier)

    def decrease_key(self, state):
        for index, s in enumerate(self.frontier):
            if s == state:
                
               # new_priority = state.heuristic()  
                self.frontier.pop(index)  # Remove the old state
                heapq.heappush(self.frontier, state)  # Insert the updated state
                break
