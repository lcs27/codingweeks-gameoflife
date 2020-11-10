import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from generate_universe import *
from simulation import *
from animation import *

if __name__=='__main__':
    #beacon_gif()
    animate((20,20),"r_pentomino",(8,8),'cool',n_generations=100,interval=100,save=True)
    print('Finished')