'''
Date: 2020-11-10 01:05:19
LastEditors: Lonel Vino
LastEditTime: 2020-11-10 01:16:47
FilePath: \gameoflife\display_universe.py
'''
from generate_universe import *
import matplotlib.pyplot as plt

#affiche l'univers avec la graine
def display_the_universe():
  seed = create_seed(type_seed="r_pentomino")
  universe = generate_universe((6,6))
  universe = add_seed_to_universe(seed, universe, x_start=1,y_start=1)
  plt.imshow(universe, cmap='Greys')
  plt.show()

#> test
if __name__ == '__main__':
  display_the_universe()
    
    