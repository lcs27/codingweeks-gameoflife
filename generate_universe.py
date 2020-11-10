import numpy as np
import matplotlib.pyplot as plt


def generate_universe(size):
    """
    Parameters
    ----------
    size :
        The size of the universe

    Returns
    -------
    universe
        The universe created
    
    """ 
    return np.zeros(size, dtype=np.int)


dict_seed = {'r_pentomino':[[0, 1, 1], [1, 1, 0], [0, 1, 0]]}

def create_seed(type_seed):
    '''
    Create the seed by the given dictionnary

    Parameters
    -------
    type_seed
        the string of the type of seed

    Returns
    -------
    seed
        the seed obtained as a numpy.array

    '''
    return np.array(dict_seed[type_seed])


def add_seed_to_universe(seed,universe,x_start=0,y_start=0):
    '''
    Add the seed to universe by replacing the corresponding places

    Parameters
    -------
    seed
        The numpy.array of the seed to add in
    universe
        The numpy.array of the universe to be added
    x_start
        The start place of the row parameter to be added(by default 0)
    y_start
        The start place of the column parameter to be added(by default 0)
    
    Returns
    -------
    universe
        the new universe that has been inserted
    
    '''
    num_rows,num_cols = seed.shape
    universe[y_start:y_start+num_rows,x_start:x_start+num_cols] = seed
    return universe

def display_universe(universe):
     '''
     To display the universe

    Parameters:
    -------
    universe
        The np.array of universe to be displayed
    '''
    plt.imshow(universe, cmap='Greys')
    plt.show()

if __name__ == "__main__":
    #print(generate_universe((4,4)))
    #print(np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]))
    #print(create_seed(type_seed = "r_pentomino"))
    pass