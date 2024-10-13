import copy
import math
class State:

    def __init__(self, state:list):
        self.state = state
        self.parent = None
        self.child = None
        self.Depth = 0
        self.heuristics = 0
        # find the zero position 
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                     self.x =i
                     self.y =j
    

                    

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.state)

    def __lt__(self,other):
        return self.heuristic() < other.heuristic()



 


    def moveup(self):
        if self.x == 0:
            return self
        newstate = State(copy.deepcopy(self.state))
        newstate.state[self.x][self.y] , newstate.state[self.x-1][self.y] = newstate.state[self.x-1][self.y],newstate.state[self.x][self.y]
        newstate.parent = self
        newstate.x = self.x -1
        self.child = newstate

        # newstate.print_puzzle()

        return newstate
    
    def movedown(self):
        if self.x == 2 :
            return self
        newstate = State(copy.deepcopy(self.state))
        newstate.state[self.x][self.y] , newstate.state[self.x+1][self.y] = newstate.state[self.x+1][self.y],newstate.state[self.x][self.y]
        newstate.parent = self
        newstate.x = self.x +1

        self.child = newstate

        # newstate.print_puzzle()

        return newstate
    
    def moveRight(self):
        if self.y == 2 :
            return self
        newstate = State(copy.deepcopy(self.state))
        newstate.state[self.x][self.y] , newstate.state[self.x][self.y+1] = newstate.state[self.x][self.y+1],newstate.state[self.x][self.y]
        newstate.parent = self
        newstate.y = self.y+1

        self.child = newstate

        # newstate.print_puzzle()
        return newstate
    

    def moveLeft(self):
        if self.y == 0:
            return self
        newstate = State(copy.deepcopy(self.state))
        newstate.state[self.x][self.y] , newstate.state[self.x][self.y-1] = newstate.state[self.x][self.y-1],newstate.state[self.x][self.y]
        newstate.parent = self
        newstate.y = self.y -1
        self.child = newstate

        # newstate.print_puzzle()

        return newstate
    

    def getchildren(self):
        children= []
        self.print_puzzle()
        temp = self.child
       
        while temp:
            
            temp.print_puzzle()
            children.append(temp)
            temp = temp.child

        return children    
    

    def print_puzzle(self):
        for row in self.state:
            print(" ".join(str(cell) for cell in row)) 
        
        print("--------------------------------------------------------")

    def get_neighbors(self):
        neighbors = []
        neighbors.append(self.moveup())
        neighbors.append(self.movedown())
        neighbors.append(self.moveRight())
        neighbors.append(self.moveLeft())
        


        return neighbors  

    def is_goalstate(self):
        goalstate = [
            [0,1,2],
            [3,4,5],
            [6,7,8]
        ]

        for i in range(3):
            for j in range(3):
                if self.state[i][j] != goalstate[i][j]:
                    return False
        return True 


       

      
    def path_search_to_goal(self,state):
        print("entering path_search_to_goal")
        path = []
        path.append(state)
        temp = state.parent
        
        
        while temp:
            
            path.append(temp)
            temp = temp.parent    

        path.reverse()
        return path
    
    

    def Manhattan_Distance(self):
        result = 0
        goal_positions = {
        0: (0, 0), 1: (0, 1), 2: (0, 2),
        3: (1, 0), 4: (1, 1), 5: (1, 2),
        6: (2, 0), 7: (2, 1), 8: (2, 2)  
        }

        for i in range(3):
            for j in range(3):
                x,y = goal_positions[self.state[i][j]]
                result+= abs(i-x)+abs(j-y)


        return int(result) 

    
    def Euclidean_Distanc(self):
        result = 0
        goal_positions = {
        0: (0, 0), 1: (0, 1), 2: (0, 2),
        3: (1, 0), 4: (1, 1), 5: (1, 2),
        6: (2, 0), 7: (2, 1), 8: (2, 2)  
        }

        for i in range(3):
            for j in range(3):
                x,y = goal_positions[self.state[i][j]]
                result += math.sqrt((i - x) ** 2 + (j - y) ** 2)


        return int(result) 
    



    def findDepth(self):
        temp = self.parent
        
        
        while temp:
            temp = temp.parent 
            self.Depth = self.Depth +1
            #print("enter loop")
        
        return self.Depth


    def GetDepth(self):
        return int(self.findDepth())
    
    def heuristic(self):
        if self.heuristics == 0:
            return self.GetDepth() + self.Manhattan_Distance()
        elif self.heuristics == 1:
            return self.GetDepth() + self.Euclidean_Distanc()
        



        

        


        

        