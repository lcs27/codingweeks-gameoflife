import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from generate_universe import *
from simulation import *
from animation import *

if __name__=='__main__':
    #beacon_gif()
    animate((20,20),"infinite",(7,7),'Greys',n_generations=30,save=True)