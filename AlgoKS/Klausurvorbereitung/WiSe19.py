import numpy as np
from random import random

def next_step(grid):
    for i in range(len(grid)):
        alive_neighbor = 0
        left = (i - 1) % len(grid)
        right = (i + 1) % len(grid)
        if grid[left] == 1:
            alive_neighbor += 1
        if grid[right] == 1:
            alive_neighbor += 1
        if grid[i] == 0 and random() <= 0.1:
            grid[i] = 1
        elif grid[i] == 1 and alive_neighbor == 2:
            grid[i] = 0
        
    
    return grid

print(next_step(np.array([1, 1, 1, 0, 0])))