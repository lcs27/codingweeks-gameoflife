import numpy as np
import matplotlib.pyplot as plt


def generate_universe(size):
    """
    Generates universe of given size with dead cells

    Parameters
    ----------
    size :
        Tuple (int, int) dimensions of the universe

    Returns
    -------
    universe
        Numpy array of the universe created; All dead cells
    
    """ 
    return np.zeros(size, dtype=np.int)


def create_seed(type_seed):
    '''
    Creates the seed by the given dictionnary

    Parameters
    -------
    type_seed
        String of the type of seed

    Returns
    -------
    seed
        Seed obtained as a numpy array

    '''
    return np.array(dict_seed[type_seed])


def add_seed_to_universe(seed,universe,y_start=0,x_start=0):
    '''
    Adds the seed to universe by replacing the corresponding places

    Parameters
    -------
    seed
        Numpy array of the seed to be added
    universe
        Numpy array of the universe to be added
    y_start
        Start place of the row parameter to be added; By default 0)
    x_start
        Start place of the column parameter to be added; By default 0)
    
    Returns
    -------
    universe
        Numpy array of the universe with seed inserted
    
    '''
    num_rows_seed,num_cols_seed = seed.shape
    num_rows_univ,num_cols_univ = universe.shape
    
    # Detect if seed violates constraints of the universe
    # If yes, return universe without seed inserted
    try:
        if num_rows_seed > num_rows_univ or num_cols_seed > num_cols_univ:
            raise ValueError("The seed is bigger than the size of the universe!")
        if y_start + num_rows_seed > num_rows_univ or x_start + num_cols_seed > num_cols_univ:
            raise ValueError("The seed is outside of the universe!")
    except:
        return universe
    
    # Insert seed and return universe with seed inserted
    universe[y_start:y_start+num_rows_seed,x_start:x_start+num_cols_seed] = seed
    return universe


def display_universe(universe):
    '''
    Displays the universe

    Parameters:
    -------
    universe
        Numpy array of universe to be displayed
    '''
    plt.imshow(universe, cmap='Greys')
    plt.show()


dict_seed = {
    "boat": [[1, 1, 0], [1, 0, 1], [0, 1, 0]],
    "r_pentomino": [[0, 1, 1], [1, 1, 0], [0, 1, 0]],
    "beacon": [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]],
    "acorn": [[0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 1, 1, 1]],
    "block_switch_engine": [
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
    ],
    "infinite": [
        [1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
    ],
    'plane':[
        [0,0,1,0,0],
        [0,1,0,1,0],
        [0,1,0,1,0],
        [0,1,0,1,0],
        [0,1,1,1,0]
    ]
}


if __name__ == "__main__":
    #print(generate_universe((4,4)))
    #print(np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]))
    #print(create_seed(type_seed = "r_pentomino"))
    pass