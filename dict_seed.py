import numpy as np

def gun():
    gun=np.zeros([11,38])
    set_1=[[5,1],[5,2],[6,1],[6,2],[3,-2],[4,-2],[3,-3],[3,-3],[5,11],
    [6,11],[7,11],[4,12],[8,12],[3,13],[9,13],[3,14],[9,14],[6,15],[4,16],
    [8,16],[5,17],[6,17],[7,17],[6,18],[3,21],[4,21],[5,21],[3,22],[4,22],
    [5,22],[2,23],[6,23],[1,25],[2,25],[6,25],[7,25]]
    for coor in set_1:
        gun[coor[0],coor[1]]=1
    return gun.T


dict_seed = {
    "boat": [[1, 1, 0], [1, 0, 1], [0, 1, 0]],
    "r_pentomino": [[0, 1, 1], [1, 1, 0], [0, 1, 0]],
    "beacon": [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]],
    "acorn": [[0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 1, 1, 1]],
    "block_switch_engine": [
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
    ],
    "infinite": [
        [1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
    ],
    'planeur':[
       [0,1,0],
       [1,1,0],
       [1,0,1]
    ],
    'line_3':[
        [1,1,1]
    ],
    'gun':gun()
}