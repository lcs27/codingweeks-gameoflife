import numpy as np

def generate_universe(size):
    return np.zeros(size, dtype=np.int)

if __name__ == "__main__":
    print(generate_universe((4,4)))
    print(np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]))