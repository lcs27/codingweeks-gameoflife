from generate_universe import *
from pytest import *
import numpy as np

def test_generate_universe():
    universe = generate_universe((4,4))
    np.testing.assert_array_equal(universe,np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]))

def test_create_seed():
    seed = create_seed(type_seed = "r_pentomino")
    np.testing.assert_array_equal(seed,np.array([[0,1,1],[1,1,0],[0,1,0]]))

def test_add_seed_to_universe():
    seed = create_seed(type_seed = "r_pentomino")
    universe = generate_universe(size=(6,6))
    universe = add_seed_to_universe(seed, universe,x_start=1, y_start=1)
    test_equality = np.array(universe == np.array([[0,0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0 ,0, 1, 0, 0, 0],
        [0 ,0, 0, 0, 0, 0],
        [0 ,0, 0, 0, 0, 0]],dtype=np.uint8))
    assert test_equality.all()

if __name__ == "__main__":
    test_generate_universe()
    test_create_seed()
    test_add_seed_to_universe()