def survival(coordinates,universe):
    '''
    Checks surrounding cells to determine if the cell will be alive or dead afterwards

    Parameters
    -------
    coordinates
        Tuple containing x and y values of the selected cell
    universe
        Initial universe containing selected cell
    
    Returns
    -------
    state of cell
        1 for alive and 0 for dead
    
    '''
    count = 0
    x = coordinates[0]
    y = coordinates[1]
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i == 0 and j == 0:
                continue
            try:
                count += universe[x+i,y+j]
            except:
                continue
    if universe[x,y] and (count == 2 or count == 3):
        return 1
    elif not universe[x,y] and count == 3:
        return 1
    else:
        return 0
