from generate_universe import *
from pytest import *


def test_generate_universe():
    assert generate_universe((4,4)) == [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

def test_create_seed():
    seed=create_seed(type_seed = "r_pentomino")
    assert seed==[[0, 1, 1], [1, 1, 0], [0, 1, 0]]

def test_add_seed_to_universe():
    seed = create_seed(type_seed = "r_pentomino")
    universe = generate_universe(size=(6,6))
    universe = add_seed_to_universe(seed, universe,x_start=1, y_start=1)
    test_equality=np.array(universe ==np.array([[0,0, 0, 0, 0, 0],
 [0, 0, 1, 1, 0, 0],
 [0, 1, 1, 0, 0, 0],
 [0 ,0, 1, 0, 0, 0],
 [0 ,0, 0, 0, 0, 0],
 [0 ,0, 0, 0, 0, 0]],dtype=np.uint8))
    assert test_equality.all()