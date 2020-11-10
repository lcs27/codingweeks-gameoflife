'''
Date: 2020-11-10 01:18:47
LastEditors: Lonel Vino
LastEditTime: 2020-11-10 01:32:40
FilePath: \gameoflife\graine.py
'''

from generate_universe import *
import numpy as np

#création de l'univers à t=0, avec la graine. Ce nouveau programme limite le nombre d'erreurs possibles (graine trop ou mal placée)

def init_universe(amorce, nombre_lignes_universe, nombre_collones_universe, place_graine_x, place_graine_y):
  seed = np.array(seeds[amorce])
  nombre_lignes_universe = max(nombre_lignes_universe, np.shape(seed)[0])
  nombre_collones_universe = max(nombre_collones_universe, np.shape(seed)[1])
  universe = generate_universe(((nombre_lignes_universe, nombre_collones_universe)))
  if place_graine_x + np.shape(seed)[0] > nombre_lignes_universe:
    print("Dimensions incompatibles. Choose an x_start between 0 and " +
          str(nombre_lignes_universe - np.shape(seed)[0]))
    place_graine_x = input()
  if place_graine_y + np.shape(seed)[1] > nombre_collones_universe:
    print("Dimensions incompatibles. Choose an y_start between 0 and " +
          str(nombre_collones_universe - np.shape(seed)[1]))
    place_graine_y = input()
  universe = add_seed_to_universe(seed, universe, place_graine_x, place_graine_y)
  return universe
