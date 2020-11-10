def survival(coordinates,universe):
    '''
    Checks surrounding cells to determine if the cell will be alive or dead afterwards

    Parameters
    -------
    coordinates
        Tuple of (y,x) of selected cell
    universe
        Initial universe containing selected cell
    
    Returns
    -------
    state of cell
        1 for alive and 0 for dead
    
    '''
    # Count the numbr of live neighbors
    count = 0
    y = coordinates[0]
    x = coordinates[1]
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i == 0 and j == 0:
                continue
            try:
                count += universe[y+i,x+j]
            except:
                continue     #if the cell has fewer tahn 8 neighbors

    #Judgement of conditions
    if universe[y,x] and (count == 2 or count == 3): #Generation
        return 1
    elif not universe[y,x] and count == 3: #Reproduction
        return 1
    else:           #the rest live cells die and dead cells remain dead
        return 0
