import numpy as np

#dictionnaire de graines
seeds = {
    "boat": [[1, 1, 0], [1, 0, 1], [0, 1, 0]],
    "r_pentomino": [[0, 1, 1], [1, 1, 0], [0, 1, 0]]
}


def generate_universe(size):
    s = np.zeros(size, dtype=np.int)
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
    
