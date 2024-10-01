from State import State
from Search import Search






if __name__ == '__main__':
    initial_state = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]
    goalstate = [
            [0,1,2],
            [3,4,5],
            [6,7,8]
        ]
    
    state = State(goalstate)
    search = Search(state)
    x= state.Euclidean_Distanc()
    print(x)


    
    

