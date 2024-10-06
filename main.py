from State import State
from Search import Search






if __name__ == '__main__':
    initial_state = [
    [5, 6, 7],
    [4, 0, 8],
    [3, 2, 1]
]
    goalstate = [
            [0,1,2],
            [3,4,5],
            [6,7,8]
        ]
    
    state = State(initial_state)
    search = Search(state)
    x= search.BFS_search()
    for x in state.path_search_to_goal(x):
        x.print_puzzle()
        print(x.Manhattan_Distance())


    
    

