from State import State
from Search import Search






if __name__ == '__main__':
    initalstate = [
        [1,2,5],
        [3,4,0],
        [6,7,8]
    ]

    
    state = State(initalstate)
    search = Search(state)
    x= search.BFS_search()
    values =  state.path_search_to_goal(x)

    for value in values:
        print (value)
        print()
        print()


    
    

