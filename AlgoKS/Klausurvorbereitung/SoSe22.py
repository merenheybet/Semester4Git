import numpy as np

rule_dict = {(0,0,0):0,
             (0,0,1):1,
             (0,1,0):1,
             (0,1,1):1,
             (1,0,0):1,
             (1,0,1):0,
             (1,1,0):0,
             (1,1,1):0}

def update_rule(grid, i, rule_dict):
    assert i < len(grid) - 1 and i > 0
    new_value = rule_dict.get((grid[i-1], grid[i], grid[i+1]))
    return new_value

def next_step(grid, rule_dict):
    new_grid = grid.copy()
    for i in range(1, len(grid)-1):
        new_grid[i] = update_rule(grid, i, rule_dict)
    return new_grid

def automaton(grid, steps, rule_dict):
    output = np.zeros((steps, len(grid)), dtype=int)
    output[0] = grid
    for i in range(steps - 1):
        output[i+1] = next_step(output[i], rule_dict)
    return output

grid = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
print(automaton(grid, 5, rule_dict))