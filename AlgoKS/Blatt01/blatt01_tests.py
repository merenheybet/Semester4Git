import pathlib
from fractions import Fraction
import numpy as np
import testsuite as ts


def disable_np_linalg():
    import numpy as np

    np.kron = ts.ForbiddenMember("np.kron")


sheet = ts.Sheet(
    1,
    tasks=[
        ts.Task(
            1,
            "arithmetic",
            description="Arithmetik Rationaler Zahlen",
            subtasks=[
                ts.Subtask(
                    "a",
                    marks=Fraction(3, 2),
                    function_name="primes_sieve",
                    description="Sieb des Eratosthenes",
                    test_cases=[
                        ts.TestCase((1,), []),
                        ts.TestCase((2,), [2]),
                        ts.TestCase((3,), [2, 3]),
                        ts.TestCase((10,), [2, 3, 5, 7]),
                        ts.TestCase((31,), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]),
                    ],
                ),
                ts.Subtask(
                    "b",
                    marks=Fraction(3, 2),
                    function_name="factorize",
                    description="Primfaktorzerlegung",
                    test_cases=[
                        ts.TestCase((1,), []),
                        ts.TestCase((2,), [2]),
                        ts.TestCase((3,), [3]),
                        ts.TestCase((4,), [2, 2]),
                        ts.TestCase((12,), [2, 2, 3]),
                        ts.TestCase((17,), [17]),
                        ts.TestCase((1155,), [3, 5, 7, 11]),
                        ts.TestCase((18150,), [2, 3, 5, 5, 11, 11]),
                    ],
                ),
                ts.Subtask(
                    "c",
                    marks=Fraction(3, 2),
                    function_name="gcd",
                    description="Euklidischer Algorithmus",
                    test_cases=[
                        ts.TestCase((5, 3), 1),
                        ts.TestCase((31, 97), 1),
                        ts.TestCase((33, 15), 3),
                        ts.TestCase((49, 77), 7),
                        ts.TestCase((136, 187), 17),
                        ts.TestCase((714, 455), 7),
                        ts.TestCase((1704, 2328), 24),
                        ts.TestCase((279, 144), 9),
                    ],
                ),
                ts.Subtask(
                    "d",
                    marks=Fraction(1),
                    function_name="qreduce",
                    description="Brüche Kürzen",
                    test_cases=[
                        ts.TestCase(((1, 17),), (1, 17)),
                        ts.TestCase(((3, 9),), (1, 3)),
                        ts.TestCase(((-15, 27),), (-5, 9)),
                        ts.TestCase(((391, 119),), (23, 7)),
                        ts.TestCase(((-1984, 512),), (-31, 8)),
                        ts.TestCase(((1191, 18),), (397, 6)),
                        ts.TestCase(((-7694, 64),), (-3847, 32)),
                        ts.TestCase(((1617, 399),), (77, 19)),
                    ],
                ),
                ts.Subtask(
                    "e",
                    marks=Fraction(3, 2),
                    function_name="qadd",
                    description="Rationale Zahlen Addieren",
                    test_cases=[
                        ts.TestCase(((4, 3), (5, 6)), (13, 6)),
                        ts.TestCase(((1, 2), (1, 7)), (9, 14)),
                        ts.TestCase(((5, 3), (4, 5)), (37, 15)),
                        ts.TestCase(((7, 8), (7, 9)), (119, 72)),
                        ts.TestCase(((51, 17), (31, 8)), (55, 8)),
                        ts.TestCase(((913, 11), (17, 15)), (1262, 15)),
                        ts.TestCase(((77, 78), (78, 77)), (12013, 6006)),
                    ],
                ),
            ],
        ),
        ts.Task(
            2,
            "linalg",
            description="Matrizen konstruieren mit NumPy",
            allowed_imports={"numpy"},
            monkeypatches=(disable_np_linalg,),
            subtasks=[
                ts.Subtask(
                    "a",
                    marks=Fraction(1),
                    function_name="reflection2d",
                    description="Spiegelungsmatrix",
                    test_cases=[
                        ts.TestCase(
                            (np.double(0.0),), np.array([[1.0, 0.0], [0.0, -1.0]])
                        ),
                        ts.TestCase((2 * np.pi,), np.array([[1.0, 0.0], [0.0, -1.0]])),
                        ts.TestCase(
                            (np.pi,),
                            np.array([[1.0, 0.0], [0.0, -1.0]]),
                        ),
                        ts.TestCase(
                            (0.25 * np.pi,),
                            np.array([[0.0, 1.0], [1.0, 0.0]]),
                        ),
                        ts.TestCase(
                            (0.5 * np.pi,),
                            np.array([[-1.0, 0.0], [0.0, 1.0]]),
                        ),
                    ],
                ),
                ts.Subtask(
                    "b",
                    marks=Fraction(1),
                    function_name="eye",
                    description="Einheitsmatrix - Rechteckig",
                    test_cases=[
                        ts.TestCase((1, 1), np.array([[1.0]])),
                        ts.TestCase(
                            (3, 2), np.array([[1.0, 0.0], [0.0, 1.0], [0.0, 0.0]])
                        ),
                        ts.TestCase(
                            (3, 4),
                            np.array(
                                [
                                    [1.0, 0.0, 0.0, 0.0],
                                    [0.0, 1.0, 0.0, 0.0],
                                    [0.0, 0.0, 1.0, 0.0],
                                ]
                            ),
                        ),
                    ],
                ),
                ts.Subtask(
                    "c",
                    marks=Fraction(1),
                    function_name="compose",
                    description="Komposition",
                    test_cases=[
                        ts.TestCase(([np.array([[1.3]])],), np.array([[1.3]])),
                        ts.TestCase(
                            (
                                [
                                    np.array([[1.0, 0.0], [0.0, 1.0]]),
                                    np.array([[2.0, 3.0], [4.0, 5.0]]),
                                ],
                            ),
                            np.array([[2.0, 3.0], [4.0, 5.0]]),
                        ),
                        ts.TestCase(
                            ([np.array([[2.0, 2.0]]), np.array([[1.0], [1.0]])],),
                            np.array([[4]]),
                        ),
                        ts.TestCase(([np.eye(3), np.zeros((3, 3))],), np.zeros((3, 3))),
                        ts.TestCase(
                            (
                                [
                                    np.diag([5.0, -1.0, 2.0]),
                                    np.ones((3, 5)),
                                    np.array([[1.3], [2.1], [-0.7], [5.2], [9.8]]),
                                ],
                            ),
                            np.array([[88.5], [-17.7], [35.4]]),
                        ),
                        ts.TestCase(
                            (
                                [
                                    np.array([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]),
                                    np.array([[1.0, 1.0], [1.0, 1.0], [1.0, 1.0]]),
                                    np.array([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]),
                                    np.array([[1.0, 1.0], [1.0, 1.0], [1.0, 1.0]]),
                                ],
                            ),
                            np.array([[18.0, 18.0], [18.0, 18.0]]),
                        ),
                    ],
                ),
                ts.Subtask(
                    "d",
                    marks=Fraction(1),
                    function_name="antidiag",
                    description="Antidiagonalmatrix",
                    test_cases=[
                        ts.TestCase(([-17.4],), np.array([[-17.4]])),
                        ts.TestCase(
                            ([2.0, 3.0, 4.0],),
                            np.array([[0, 0, 4.0], [0, 3.0, 0], [2.0, 0, 0]]),
                        ),
                        ts.TestCase(
                            ([2.0, 3.0, 4.0, 5.0],),
                            np.array(
                                [
                                    [0.0, 0.0, 0.0, 5.0],
                                    [0, 0, 4.0, 0.0],
                                    [0, 3.0, 0, 0],
                                    [2.0, 0, 0, 0],
                                ]
                            ),
                        ),
                    ],
                ),
                ts.Subtask(
                    "e",
                    marks=Fraction(3, 2),
                    function_name="kronecker_product",
                    description="Kronecker-Matrix-Produkt",
                    test_cases=[
                        ts.TestCase(
                            (
                                np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]),
                                np.array([[7.0, 8.0], [9.0, 0.0]]),
                            ),
                            np.array(
                                [
                                    [7.0, 8.0, 14.0, 16.0],
                                    [9.0, 0.0, 18.0, 0.0],
                                    [21.0, 24.0, 28.0, 32.0],
                                    [27.0, 0.0, 36.0, 0.0],
                                    [35.0, 40.0, 42.0, 48.0],
                                    [45.0, 0.0, 54.0, 0.0],
                                ]
                            ),
                        ),
                        ts.TestCase(
                            (np.array([[2.0]]), np.array([[3.0, 4.0], [5.0, 6.0]])),
                            np.array([[6.0, 8.0], [10.0, 12.0]]),
                        ),
                        ts.TestCase(
                            (
                                np.array([[2.0]]),
                                np.array([[2.0, 4.0], [1.0, 0], [0, 1.0]]),
                            ),
                            np.array([[4.0, 8.0], [2.0, 0], [0, 2.0]]),
                        ),
                    ],
                ),
                ts.Subtask(
                    "f",
                    marks=Fraction(3, 2),
                    function_name="walsh",
                    description="Walsh-Matrix",
                    test_cases=[
                        ts.TestCase((0,), np.array([[1.0]])),
                        ts.TestCase((1,), np.array([[1.0, 1.0], [1.0, -1.0]])),
                        ts.TestCase(
                            (2,),
                            np.array(
                                [
                                    [1.0, 1.0, 1.0, 1.0],
                                    [1.0, -1.0, 1.0, -1.0],
                                    [1.0, 1.0, -1.0, -1.0],
                                    [1.0, -1.0, -1.0, 1.0],
                                ]
                            ),
                        ),
                    ],
                ),
            ],
        ),
        ts.Task(
            3,
            "gameoflife",
            description="Game of Life",
            allowed_imports={"numpy"},
            subtasks=[
                ts.Subtask(
                    "a",
                    marks=Fraction(2),
                    function_name="add_entity",
                    description="Initialisierung",
                    test_cases=[
                        ts.TestCase(
                            (
                                np.array([[0]], dtype=bool),
                                np.array([[1]], dtype=bool),
                                0,
                                0,
                            ),
                            np.array([[1]], dtype=bool),
                        ),
                        ts.TestCase(
                            (
                                np.array([[0, 0, 0], [0, 0, 0]], dtype=bool),
                                np.array([[1]], dtype=bool),
                                0,
                                1,
                            ),
                            np.array([[0, 1, 0], [0, 0, 0]], dtype=bool),
                        ),
                        ts.TestCase(
                            (
                                np.array([[0, 0, 0], [0, 0, 0]], dtype=bool),
                                np.array([[1,1]], dtype=bool),
                                0,
                                1,
                            ),
                            np.array([[0, 1, 1], [0, 0, 0]], dtype=bool),
                        ),
                        ts.TestCase(
                            (
                                np.array([[0, 0, 0], [0, 0, 0]], dtype=bool),
                                np.array([[1,1],[1,1]], dtype=bool),
                                0,
                                1,
                            ),
                            np.array([[0, 1, 1], [0, 1, 1]], dtype=bool),
                        ),
                        # Test Case 5: Entity (2x2 block) added at bottom-right corner
                        ts.TestCase(
                            (
                                np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]], dtype=bool),
                                np.array([[1, 1], [1, 0]], dtype=bool),
                                1,
                                1,
                            ),
                            np.array([[0, 0, 0], [0, 1, 1], [0, 1, 0]], dtype=bool),
                        ),

                        # Test Case 6: Adding a glider to a 5x5 grid at top-left
                        ts.TestCase(
                            (
                                np.zeros((5, 5), dtype=bool),
                                np.array([[0, 1, 0],
                                        [0, 0, 1],
                                        [1, 1, 1]], dtype=bool),
                                0,
                                0,
                            ),
                            np.array([
                                [0, 1, 0, 0, 0],
                                [0, 0, 1, 0, 0],
                                [1, 1, 1, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                            ], dtype=bool),
                        ),

                        # Test Case 7: Entity with 1 column, multiple rows
                        ts.TestCase(
                            (
                                np.array([[0, 0], [0, 0], [0, 0]], dtype=bool),
                                np.array([[1], [0], [1]], dtype=bool),
                                0,
                                1,
                            ),
                            np.array([[0, 1], [0, 0], [0, 1]], dtype=bool),
                        ),

                        # Test Case 8: Placing an empty (0x0) entity (should not change the grid)
                        ts.TestCase(
                            (
                                np.array([[0, 0], [0, 0]], dtype=bool),
                                np.empty((0, 0), dtype=bool),
                                0,
                                0,
                            ),
                            np.array([[0, 0], [0, 0]], dtype=bool),
                        ),

                        #   TODO More tests
                    ],
                ),
                ts.Subtask(
                    "b",
                    marks=Fraction(4),
                    function_name="next_step",
                    description="Zeitschritt",
                    test_cases=[
                        ts.TestCase(
                            (np.array([[1]], dtype=bool),), np.array([[0]], dtype=bool)
                        ),
                        ts.TestCase(
                            (np.array([[0]], dtype=bool),), np.array([[0]], dtype=bool)
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [
                                        [0, 0, 0, 0],
                                        [0, 1, 0, 0],
                                        [0, 0, 1, 0],
                                        [1, 1, 1, 0],
                                    ],
                                    dtype=bool,
                                ),
                            ),
                            np.array(
                                [
                                    [1, 0, 1, 0],
                                    [0, 0, 0, 0],
                                    [1, 0, 1, 1],
                                    [0, 1, 1, 1],
                                ],
                                dtype=bool,
                            ),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [
                                        [1, 0, 1, 0],
                                        [0, 0, 0, 0],
                                        [1, 0, 1, 1],
                                        [0, 1, 1, 1],
                                    ],
                                    dtype=bool,
                                ),
                            ),
                            np.array(
                                [
                                    [1, 0, 1, 0],
                                    [1, 0, 1, 0],
                                    [1, 0, 0, 0],
                                    [0, 0, 0, 0],
                                ],
                                dtype=bool,
                            ),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [
                                        [1, 0, 1, 0],
                                        [1, 0, 1, 0],
                                        [1, 0, 0, 0],
                                        [0, 0, 0, 0],
                                    ],
                                    dtype=bool,
                                ),
                            ),
                            np.array(
                                [
                                    [0, 0, 0, 0],
                                    [1, 0, 0, 0],
                                    [0, 1, 0, 1],
                                    [0, 1, 0, 1],
                                ],
                                dtype=bool,
                            ),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [
                                        [1, 0, 1, 0],
                                        [1, 0, 1, 0],
                                        [1, 0, 0, 0],
                                        [0, 0, 0, 0],
                                    ],
                                    dtype=bool,
                                ),
                            ),
                            np.array(
                                [
                                    [0, 0, 0, 0],
                                    [1, 0, 0, 0],
                                    [0, 1, 0, 1],
                                    [0, 1, 0, 1],
                                ],
                                dtype=bool,
                            ),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [
                                        [0, 0, 0, 0],
                                        [1, 0, 0, 0],
                                        [0, 1, 0, 1],
                                        [0, 1, 0, 1],
                                    ],
                                    dtype=bool,
                                ),
                            ),
                            np.array(
                                [
                                    [1, 0, 0, 0],
                                    [1, 0, 0, 0],
                                    [0, 1, 0, 1],
                                    [0, 0, 0, 0],
                                ],
                                dtype=bool,
                            ),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [
                                        [1, 0, 0, 0],
                                        [1, 0, 0, 0],
                                        [0, 1, 0, 1],
                                        [0, 0, 0, 0],
                                    ],
                                    dtype=bool,
                                ),
                            ),
                            np.array(
                                [
                                    [0, 0, 0, 0],
                                    [1, 1, 0, 1],
                                    [1, 0, 0, 0],
                                    [1, 0, 0, 0],
                                ],
                                dtype=bool,
                            ),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [
                                        [0, 0, 0, 0],
                                        [1, 1, 0, 1],
                                        [1, 0, 0, 0],
                                        [1, 0, 0, 0],
                                    ],
                                    dtype=bool,
                                ),
                            ),
                            np.array(
                                [
                                    [0, 1, 0, 1],
                                    [1, 1, 0, 1],
                                    [0, 0, 0, 0],
                                    [0, 0, 0, 0],
                                ],
                                dtype=bool,
                            ),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [
                                        [0, 1, 0, 1],
                                        [1, 1, 0, 1],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0],
                                    ],
                                    dtype=bool,
                                ),
                            ),
                            np.array(
                                [
                                    [0, 1, 0, 1],
                                    [0, 1, 0, 1],
                                    [1, 0, 0, 0],
                                    [0, 0, 0, 0],
                                ],
                                dtype=bool,
                            ),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [
                                        [0, 1, 0, 1],
                                        [0, 1, 0, 1],
                                        [1, 0, 0, 0],
                                        [0, 0, 0, 0],
                                    ],
                                    dtype=bool,
                                ),
                            ),
                            np.array(
                                [
                                    [0, 0, 0, 0],
                                    [0, 1, 0, 1],
                                    [1, 0, 0, 0],
                                    [1, 0, 0, 0],
                                ],
                                dtype=bool,
                            ),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [
                                        [0, 0, 0, 0],
                                        [0, 1, 0, 1],
                                        [1, 0, 0, 0],
                                        [1, 0, 0, 0],
                                    ],
                                    dtype=bool,
                                ),
                            ),
                            np.array(
                                [
                                    [1, 0, 0, 0],
                                    [1, 0, 0, 0],
                                    [1, 1, 0, 1],
                                    [0, 0, 0, 0],
                                ],
                                dtype=bool,
                            ),
                        ),
                    ],
                ),
            ],
        ),
    ],
)


def jupyter_run_tests(*tasknames: str):
    src_dir = pathlib.Path(__file__).parent
    ts.TestDriver(sheet, src_dir).run_jupyter(tasknames)


if __name__ == "__main__":
    src_dir = pathlib.Path.cwd()
    ts.TestDriver(sheet, src_dir).run_cli()
