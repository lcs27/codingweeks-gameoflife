from rules import *
from generate_universe import *

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

#Test code
if __name__ == '__main__':
    test_survival()