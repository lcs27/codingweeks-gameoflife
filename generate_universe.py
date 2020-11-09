'''
Date: 2020-11-09 15:13:17
LastEditors: Lonel Vino
LastEditTime: 2020-11-09 22:05:03
FilePath: \gameoflife\generate_universe.py
'''


import numpy as np
from seeds import seeds

#dictionnaire de graines

def generate_universe(size):
    s = np.zeros((size[0], size[1]), dtype=np.int)
    return s

#création d'une graine à partir du dictionnaire de graines
def create_seed(type_seed):
    return np.array(seeds[type_seed])

#ajoute la graine dans l'universà la place x_start, y_start
def add_seed_to_universe(seed,universe, x_start, y_start):
    (n,p)=np.shape(seed)
    for i in range(n):
        for j in range(p):
            universe[x_start+i,y_start+j]=seed[0+i,0+j]
    return universe

### test code
if __name__ == '__main__':
    s = generate_universe((3,2))
    print(s)
    
