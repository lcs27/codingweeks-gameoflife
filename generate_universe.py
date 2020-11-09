import numpy as np

def generate_universe(size):
    s = np.zeros(size, dtype=np.int)
    return s

### test code
if __name__ == '__main__':
    s = generate_universe((3,2))
    print(s)
    
