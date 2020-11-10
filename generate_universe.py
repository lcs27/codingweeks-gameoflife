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
    #Exception detect
    num_rows_seed,num_cols_seed = seed.shape
    num_rows_univ,num_cols_univ = universe.shape
    try:
        if num_rows_seed > num_rows_univ or num_cols_seed > num_cols_univ:
            raise ValueError("The seed is bigger than the size of the universe!")
    except:
        return universe
        #compte = 0
    excy = num_rows_seed + y_start - num_rows_univ
    excx = num_cols_seed + x_start - num_cols_univ
        #while compte + y_start < num_rows_univ and compte + x_start < num_cols_univ:
    if  num_rows_univ >= y_start+num_rows_seed and num_cols_univ >= x_start+num_cols_seed:
        universe[y_start:y_start+num_rows_seed,x_start:x_start+num_cols_seed] = seed
    elif num_rows_univ < y_start+num_rows_seed and num_cols_univ > x_start+num_cols_seed:
        universe[y_start:num_rows_univ,x_start:x_start+num_cols_seed]=seed[0:num_rows_seed-excy,0:num_cols_seed]
        universe[0:excy,0:num_rows_univ]=seed[excy:num_rows_seed,0]
    elif num_rows_univ < y_start+num_rows_seed and num_cols_univ < x_start+num_cols_seed:
        universe[y_start:y_start+num_rows_seed,x_start:num_rows_univ]=seed[0:num_rows_seed,0:num_cols_seed-excx]
        universe[0:num_cols_univ,0:excx]=seed[0,excx:num_cols_seed]
        
        #universe[min(y_start:num_rows_univ,y_start:num_rows_seed),min(x_start:num_cols_univ,x_start:num_cols_seed)]=seed[0:num_rows_seed-excy,0:num_cols_seed-excx]
        #universe[0:excy,0:excx]=seed[excy:num_rows_seed,excx:num_cols_seed]
    print(universe[1:3,2:4])
        
    #else:
     #   universe[y_start:y_start+num_rows_seed,x_start:x_start+num_cols_seed] = seed
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
}


if __name__ == "__main__":
    universe=generate_universe([6,6])
    #print(np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]))
    #print(create_seed(type_seed = "r_pentomino"))
    print(add_seed_to_universe(create_seed("boat"),universe,4,0))
    
