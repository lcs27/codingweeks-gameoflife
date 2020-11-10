from simulation import *
from generate_universe import *
import numpy as np

def test_survival():
    #Generation of a universe
    seed = create_seed(type_seed = "r_pentomino")
    universe = generate_universe(size=(6,6))
    universe = add_seed_to_universe(seed, universe,x_start=1, y_start=1)
    '''
    The universe is:
    Po:0,1,2,3,4,5
     0[0,0,0,0,0,0],
     1[0,0,1,1,0,0],
     2[0,1,1,0,0,0],
     3[0,0,1,0,0,0],
     4[0,0,0,0,0,0],
     5[0,0,0,0,0,0] 
    '''

    #Reproduction: A dead cell with exactly three live neighbours becomes a live cell.
    assert survival((1,1),universe) == 1
    #No change: A dead celle remains dead with only 2 live celles around it
    assert survival((3,3),universe) == 0
    #Generation: A live cell with two or three live neighbours lives on to the next generation.
    assert survival((1,2),universe) == 1#three live neighbours
    assert survival((1,3),universe) == 1#two live neighbours
    #Overpopulation: A live cell with more than three live neighbours dies.
    universe[2,0] = 1
    universe[3,1] = 1
    '''
    The universe is:
    Po:0,1,2,3,4,5
     0[0,0,0,0,0,0],
     1[0,0,1,1,0,0],
     2[1,1,1,0,0,0],
     3[0,1,1,0,0,0],
     4[0,0,0,0,0,0],
     5[0,0,0,0,0,0] 
    '''
    assert survival((3,1),universe) == 0
    #Underpopulation: A live cell with fewer than two live neighbours dies.
    universe[1,2] = 0
    '''
    The universe is:
    Po:0,1,2,3,4,5
     0[0,0,0,0,0,0],
     1[0,0,0,1,0,0],
     2[1,1,1,0,0,0],
     3[0,1,1,0,0,0],
     4[0,0,0,0,0,0],
     5[0,0,0,0,0,0]
    '''
    assert survival((1,3),universe) == 0

def test_generation():
    # Generation of all cells in an universe
    # Generation with seed "r_pentomino"
    test_seed_1 = create_seed(type_seed = "r_pentomino")
    test_universe_1 = generate_universe(size=(6, 6))
    test_universe_1 = add_seed_to_universe(test_seed_1, test_universe_1,x_start=1, y_start=1)
    test_universe_1 = generation(test_universe_1)
    '''
    Po:0,1,2,3,4,5
     0[0,0,0,0,0,0],
     1[0,0,1,1,0,0],
     2[0,1,1,0,0,0],
     3[0,0,1,0,0,0],
     4[0,0,0,0,0,0],
     5[0,0,0,0,0,0] 
    '''
    test_equality_1 = np.array(test_universe_1 == np.array([[0 , 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]],dtype=np.uint8))
    assert test_equality_1.all()

def test_simulate():
    initial_universe = generate_universe(size=(6, 6))
    test_seed_1 = create_seed(type_seed = "r_pentomino")
    initial_universe = add_seed_to_universe(test_seed_1, initial_universe,x_start=1, y_start=1)
    
    # Zero time
    test_universe_0 = game_life_simulate(initial_universe,0)
    test_equality_0 = np.array(test_universe_0 == np.array([[0 , 0, 0, 0, 0, 0],
        [0 , 0, 1, 1, 0, 0],
        [0 , 1, 1, 0, 0, 0],
        [0 , 0, 1, 0, 0, 0],
        [0 , 0, 0, 0, 0, 0],
        [0 , 0, 0, 0, 0, 0]],dtype=np.uint8))
    assert test_equality_0.all()
    
    # One time
    test_universe_1 = game_life_simulate(initial_universe,1)
    test_equality_1 = np.array(test_universe_1 == np.array([[0 , 0, 0, 0, 0, 0],
        [0 , 1, 1, 1, 0, 0],
        [0 , 1, 0, 0, 0, 0],
        [0 , 1, 1, 0, 0, 0],
        [0 , 0, 0, 0, 0, 0],
        [0 , 0, 0, 0, 0, 0]],dtype=np.uint8))
    assert test_equality_1.all()
    
    #Two times
    test_universe_2 = game_life_simulate(initial_universe,2)
    test_equality_2 = np.array(test_universe_2 == np.array([[0, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 0],
        [0 ,1, 1, 0, 0, 0],
        [0 ,0, 0, 0, 0, 0],
        [0 ,0, 0, 0, 0, 0]],dtype=np.uint8))
    assert test_equality_2.all()


#Test code
if __name__ == '__main__':
    test_survival()
    test_generation()
    test_simulate()
