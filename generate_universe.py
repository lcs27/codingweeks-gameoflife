import numpy as np
import matplotlib.pyplot as plt

def generate_universe(size):
    return np.zeros(size, dtype=np.int)

dict_seed = {'r_pentomino':[[0, 1, 1], [1, 1, 0], [0, 1, 0]]}

def create_seed(type_seed):
  return np.array(dict_seed[type_seed])

def add_seed_to_universe(seed,universe,x_start=0,y_start=0):
    num_rows,num_cols = seed.shape
    universe[y_start:y_start+num_rows,x_start:x_start+num_cols] = seed
    return universe

def display_universe(universe):
    plt.imshow(universe)
    plt.show()

if __name__ == "__main__":
    #print(generate_universe((4,4)))
    #print(np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]))
    #print(create_seed(type_seed = "r_pentomino"))
    pass