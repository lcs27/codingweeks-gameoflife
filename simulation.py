import numpy as np


def survival(coordinates,universe):
    '''
    Checks surrounding cells to determine if the cell will be alive or dead afterwards

    Parameters
    -------
    coordinates
        Tuple (y,x) of selected cell
    universe
        Numpy array of initial universe containing selected cell
    
    Returns
    -------
    final state of cell
        1 for alive and 0 for dead
    
    '''
    
    # Count the number of live neighbours
    count = 0
    y = coordinates[0]
    x = coordinates[1]
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i == 0 and j == 0:
                continue # Do not include cell whose neighbours are to be checked
            try:
                count += universe[y+i,x+j]
            except:
                continue # Neighbour cell does not exist (i.e. out of universe boundary)

    # Judge survivability
    if universe[y,x] and (count == 2 or count == 3): # Live cell stays alive
        return 1
    elif not universe[y,x] and count == 3: # Dead cell becomes alive
        return 1
    else: # All other conditions that lead to a dead cell afterwards
        return 0


def generation(universe):
    '''
    Generates the next iteration of the universe

    Parameters
    -------
    universe
        Numpy array of initial universe on which the next iteration is to be generated
    
    Returns
    --------
    new_universe
        Numpy array of the new universe obtained
    
    '''
    # Identify size of given universe
    num_rows_univ,num_cols_univ = universe.shape

    # Create a new universe on which values derived from the survival function on given universe are later added
    new_universe = np.zeros([num_rows_univ,num_cols_univ])
    for i in range(0,num_rows_univ):
        for j in range(0,num_cols_univ):
            new_universe[i,j] = survival((i,j),universe)
    return new_universe


def game_life_simulate(universe, iterations):
    '''
    Simulation of the game over given number of iterations
    
    Parameters
    -------
    universe
        Numpy array of initial universe
    iterations
        Integer of the number of iterations to be generated

    Returns
    --------
    latest_universe
        Numpy array of final universe
    '''
    # Return given universe if no iteration is requested
    if iterations == 0:
        return universe

    # Loop over the given number of iterations to generate latest universe.
    latest_universe = None
    for i in range(0,iterations):
        latest_universe = generation(universe)
        universe = latest_universe
    return latest_universe