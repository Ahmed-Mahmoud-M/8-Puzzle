import copy
class State:

    def __init__(self, state:list):
        self.state = state
        self.parent = None
        self.child = None
        # find the zero position 
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                     self.x =i
                     self.y =j

                    




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


    def moveup(self):
        if self.x == 0:
            return None
        newstate = State(copy.deepcopy(self.state))
        newstate.state[self.x][self.y] , newstate.state[self.x-1][self.y] = newstate.state[self.x-1][self.y],newstate.state[self.x][self.y]
        newstate.parent = self.state
        newstate.x = self.x -1
        self.child = newstate

        # newstate.print_puzzle()

        return newstate
    
    def movedown(self):
        if self.x == 2 :
            return None
        newstate = State(copy.deepcopy(self.state))
        newstate.state[self.x][self.y] , newstate.state[self.x+1][self.y] = newstate.state[self.x+1][self.y],newstate.state[self.x][self.y]
        newstate.parent = self.state
        newstate.x = self.x +1

        self.child = newstate

        # newstate.print_puzzle()

        return newstate
    
    def moveRight(self):
        if self.y == 2 :
            return None
        newstate = State(copy.deepcopy(self.state))
        newstate.state[self.x][self.y] , newstate.state[self.x][self.y+1] = newstate.state[self.x][self.y+1],newstate.state[self.x][self.y]
        newstate.parent = self.state
        newstate.y = self.y+1

        self.child = newstate

        # newstate.print_puzzle()
        return newstate
    

    def moveLeft(self):
        if self.y == 0:
            return None
        newstate = State(copy.deepcopy(self.state))
        newstate.state[self.x][self.y] , newstate.state[self.x][self.y-1] = newstate.state[self.x][self.y-1],newstate.state[self.x][self.y]
        newstate.parent = self.state
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
        


       

      



        

        


        

        