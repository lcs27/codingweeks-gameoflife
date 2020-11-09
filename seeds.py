'''
Date: 2020-11-09 21:54:23
LastEditors: Lonel Vino
LastEditTime: 2020-11-09 22:04:21
FilePath: \gameoflife\seeds.py
'''
seeds = {
    "boat": [[1, 1, 0], [1, 0, 1], [0, 1, 0]],
    "r_pentomino": [[0, 1, 1], [1, 1, 0], [0, 1, 0]],
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
    "block": [[1, 1],
              [1, 1],
              ],
    "beacon": [
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1],
    ],
    "loaf": [[0, 1, 1, 0],
             [1, 0, 0, 1],
             [0, 1, 0, 1],
             [0, 0, 1, 0],
             ],
    "beehive": [[0, 1, 1, 0],
                [1, 0, 0, 1],
                [0, 1, 1, 0],
                ],
    "toad": [[0, 1, 1, 1],
             [1, 1, 1, 0],
             ],
    "tub": [[0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
            ],
}
