from State import State
from UnInformedSearch import *
from InformedSearch import *






if __name__ == '__main__':
    initial_state = [
    [1, 0, 2],
    [3, 4, 5],
    [6, 7, 8]
]
    goalstate = [
            [0,1,2],
            [3,4,5],
            [6,7,8]
        ]
    
    state = State(initial_state)
    print(state.GetDepth())
    print(state.Manhattan_Distance())
    search = InformedSearch(state)
    x= search.Astar()
    for x in state.path_search_to_goal(x):
        x.print_puzzle()
        print("Depth level :" ,x.GetDepth())


    
    

