import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from generate_universe import *
from simulation import *

def beacon_gif():
    universe = generate_universe(size=(6, 6))
    seed = create_seed(type_seed = "beacon")
    universe = add_seed_to_universe(seed,universe,x_start=1,y_start=1)    
    fig = plt.figure()
    im = plt.imshow(universe, cmap='Greys', animated = True)
    def update(i):
        im.set_array(game_life_simulate(universe,i))
        return im,
    ani = anim.FuncAnimation(fig, update, frames=24, interval = 500, blit = True)
    plt.show()

    
def animate(universe,cmap,n_generations,interval,save=False,path=None):
    '''
    The basic animation of game_of_life

    Parameters
    --------
    :param universe
        Array of initial universe on which the next iteration is to be generated
    :param cmap: 
        (str) the matplotlib cmap that should be used
    :param n_generations: 
        (int) number of universe iterations, defaults to 30
    :param interval: 
        (int )time interval between updates (milliseconds), defaults to 300ms
    :param save: 
        (bool) whether the animation should be saved, defaults to False
    '''
