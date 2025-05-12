#!/usr/bin/env python3

import numpy as np


glider = np.array([[0,1,0],
                   [0,0,1],
                   [1,1,1]],
                  dtype=bool)


c10orthogonal = np.array([[0,1,1,0,0,1,1,0],
                          [0,0,0,1,1,0,0,0],
                          [0,0,0,1,1,0,0,0],
                          [1,0,1,0,0,1,0,1],
                          [1,0,0,0,0,0,0,1],
                          [0,0,0,0,0,0,0,0],
                          [1,0,0,0,0,0,0,1],
                          [0,1,1,0,0,1,1,0],
                          [0,0,1,1,1,1,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,1,1,0,0,0],
                          [0,0,0,1,1,0,0,0]],
                         dtype=bool)


def gamegrid(w, h, entities):
    """Creates the game grid on which the Game of Life is to be executed.

    Args:
        w (int): Width of the grid.
        h (int): Height of the grid.
        entities (List[Tuple[np.ndarray, int, int]]):
            List of start entities together with their initial positions that
            are to be placed at the specified position on the grid. You may
            safely assume, that the positional entries in the list do not
            break the boundaries of the game grid.

    Returns:
        np.ndarray: The game grid modelled as an (h, w) numpy-array of type
        ``bool``.
    """
    grid = np.zeros((h,w), dtype=bool)
    for (entity, x, y) in entities:
        add_entity(grid, entity, x, y)
    return grid


def add_entity(grid, entity, y, x):
    """Adds an ``entity`` to the given ``grid`` at the specified position.

    Args:
        grid (np.ndarray): The original game grid.
        entity (np.ndarray): The entity that should be added.
        y (int): The y-position the entity shall be added at.
        x (int): The x-position the entity shall be added at.

    Returns:
        np.ndarray: The updated game grid with the entity starting at position
        (y, x).
    """
    entity_y_size, entity_x_size = np.shape(entity)
    for y_offset in range(entity_y_size):
        for x_offset in range(entity_x_size):
            grid[y+y_offset, x+x_offset] = entity[y_offset, x_offset] 

    return grid


def next_step(grid):
    """Updates the game grid ``grid`` according to the game rules.

    Args:
        grid (np.ndarray): The game grid.

    Returns:
        np.ndarray: The game grid after one time step. You can read the
        rules according to which you should update each cell in your
        exercise sheet.
    """
    y_size, x_size = np.shape(grid)
    duplicate_grid = np.copy(grid)

    for y_index in range(y_size):
        for x_index in range(x_size):
            current_cell = grid[y_index, x_index]
            upper_left = int(grid[(y_index - 1) % y_size, (x_index - 1) % x_size])
            upper = int(grid[(y_index - 1) % y_size, x_index])
            upper_right = int(grid[(y_index - 1) % y_size, (x_index + 1) % x_size])
            left = int(grid[y_index, (x_index - 1) % x_size])
            right = int(grid[y_index, (x_index + 1) % x_size])
            lower_left = int(grid[(y_index + 1) % y_size, (x_index - 1) % x_size])
            lower = int(grid[(y_index + 1) % y_size, x_index])
            lower_right = int(grid[(y_index + 1) % y_size, (x_index + 1) % x_size])

            total_neighbors = upper_left + upper + upper_right + left + right + lower_left + lower + lower_right

            if total_neighbors == 3:
                add_entity(duplicate_grid, np.array([[1]], dtype=bool), y_index, x_index)
            elif current_cell and (total_neighbors < 2):
                add_entity(duplicate_grid, np.array([[0]], dtype=bool), y_index, x_index)
            elif current_cell and (total_neighbors == 2):
                continue
            elif total_neighbors > 3:
                add_entity(duplicate_grid, np.array([[0]], dtype=bool), y_index, x_index)

    return duplicate_grid



