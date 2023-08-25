from functions import checkfullsolution, arraysgenerator, fillallonezeros, findoptions
import numpy as np


puzzle = np.array([
    [0, 0, 2, 3, 0, 0, 0, 0, 4],
    [0, 8, 0, 0, 6, 9, 0, 0, 0],
    [4, 5, 9, 2, 0, 7, 1, 6, 0],
    [1, 4, 5, 0, 9, 2, 0, 3, 8],
    [6, 7, 0, 0, 1, 0, 0, 4, 0],
    [2, 0, 0, 0, 0, 0, 6, 5, 1],
    [0, 1, 7, 0, 0, 6, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 5],
    [8, 0, 4, 5, 0, 0, 0, 1, 0]
])

puzzle2 = np.array([
    [7, 0, 9, 4, 0, 0, 0, 6, 8],
    [0, 0, 0, 0, 2, 0, 0, 4, 0],
    [0, 0, 3, 0, 0, 0, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 5, 0, 0],
    [8, 0, 4, 2, 0, 0, 0, 0, 9],
    [0, 3, 0, 7, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 0, 0, 0, 0, 6],
    [6, 0, 7, 0, 5, 0, 9, 0, 0]
])


fillallonezeros(puzzle2)

print(puzzle2)

findoptions(puzzle2)
