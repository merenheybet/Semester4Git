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
    pass  # TODO


def next_step(grid):
    """Updates the game grid ``grid`` according to the game rules.

    Args:
        grid (np.ndarray): The game grid.

    Returns:
        np.ndarray: The game grid after one time step. You can read the
        rules according to which you should update each cell in your
        exercise sheet.
    """
    pass  # TODO
