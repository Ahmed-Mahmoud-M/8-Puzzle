from State import State






if __name__ == '__main__':
    initalstate = [
        [1,2,5],
        [3,4,0],
        [6,7,8]
    ]

    state = State(initalstate)
    
    # x=state.moveup()
    y= state.moveup()
    x = y.moveLeft()
    z = x.moveLeft()

    # w = z.moveRight()

    state.getchildren()

