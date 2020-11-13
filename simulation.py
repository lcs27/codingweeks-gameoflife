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
    num_rows_univ,num_cols_univ = universe.shape
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i == 0 and j == 0:
                continue # Do not include cell whose neighbours are to be checked
            modified_y = (y + i) % num_rows_univ # Implement torroidal universe
            modified_x = (x + j) % num_cols_univ # Implement torroidal universe
            count += universe[modified_y,modified_x] 

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


def game_life_simulate(universe, iterations, universe_dict):
    '''
    Simulation of the game over given number of iterations
    
    Parameters
    -------
    universe
        Numpy array of initial universe
    iterations
        Integer of the number of iterations to be generated
    universe_dict
        Dictionary containing the number of iterations as key and generated universe as value

    Returns
    --------
    latest_universe
        Numpy array of final universe
    
    '''
    # Return given universe if no iteration is requested
    if iterations == 0:
        return universe

    # # Loop over the given number of iterations to generate latest universe.
    # latest_universe = None
    # for i in range(0,iterations):
    #     latest_universe = generation(universe)
    #     universe = latest_universe
    # return latest_universe

    # Return generated universe if it already exists in universe_dict.
    elif iterations in universe_dict:
        return universe_dict[iterations]

    # Use of recursion and memoisation to generate latest universe.
    else:
        universe_dict[iterations] = generation(game_life_simulate(universe,iterations - 1,universe_dict))
        return universe_dict[iterations]


def reset_universe_dict(universe_dict):
    '''
    Resets universe_dict for correct usage of game_life_simulate

    Parameters
    -------
    universe_dict
        universe_dict generated by previous usage of game_life_simulate
    
    Returns
    -------
    universe_dict
        universe_dict reset
    
    '''
    universe_dict = {}


universe_dict = {}