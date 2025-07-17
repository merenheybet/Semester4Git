import pathlib
from fractions import Fraction
import numpy as np
import testsuite as ts


def cb1(j):
    return [(1, j)]


def cb2(j):
    return [((-1) ** j, 4 - j - 1)]


def cb3(j):
    return [((-1) ** i, i) for i in sorted((j, 6 - j - 1))]


def cb4(j):
    return [(1, j)] if j % 2 == 0 else []


def c0(x, y):
    return 0.0


def cm1(x, y):
    return -1.0


def c10(x, y):
    return 10.0


def discont1(x, y):
    return 1.0 if x == 1 else 0.0


def lin_y(x, y):
    return y


def m6x(x, y):
    return -6.0 * x


def x_cubed(x, y):
    return x**3


def x_half(x, y):
    return 0.5 * x


sheet = ts.Sheet(
    9,
    tasks=[
        ts.Task(
            1,
            "sparse_linalg",
            "Dünnbesetzte Lineare Algebra",
            allowed_imports={"numpy"},
            subtasks=[
                ts.Subtask(
                    "a",
                    marks=Fraction(2),
                    function_name="crs_assemble",
                    description="CRS-Matrix erzeugen",
                    test_cases=[
                        ts.TestCase(
                            (3, cb1),
                            ts.Cls(
                                "CrsMatrix",
                                val=np.array([1.0, 1.0, 1.0]),
                                col_idx=np.array([0, 1, 2]),
                                row_ptr=np.array([0, 1, 2, 3]),
                            ),
                        ),
                        ts.TestCase(
                            (4, cb2),
                            ts.Cls(
                                "CrsMatrix",
                                val=np.array([1.0, -1.0, 1.0, -1.0]),
                                col_idx=np.array([3, 2, 1, 0]),
                                row_ptr=np.array([0, 1, 2, 3, 4]),
                            ),
                        ),
                        ts.TestCase(
                            (6, cb3),
                            ts.Cls(
                                "CrsMatrix",
                                val=np.array(
                                    [
                                        1.0,
                                        -1.0,
                                        -1.0,
                                        1.0,
                                        1.0,
                                        -1.0,
                                        1.0,
                                        -1.0,
                                        -1.0,
                                        1.0,
                                        1.0,
                                        -1.0,
                                    ]
                                ),
                                col_idx=np.array([0, 5, 1, 4, 2, 3, 2, 3, 1, 4, 0, 5]),
                                row_ptr=np.array([0, 2, 4, 6, 8, 10, 12]),
                            ),
                        ),
                        ts.TestCase(
                            (4, cb4),
                            ts.Cls(
                                "CrsMatrix",
                                val=np.array([1.0, 1.0]),
                                col_idx=np.array([0, 2]),
                                row_ptr=np.array([0, 1, 1, 2, 2]),
                            ),
                        ),
                    ],
                ),
                ts.Subtask(
                    "b",
                    marks=Fraction(1),
                    function_name="crs_mvm",
                    description="CRS Matrix-Vektor-Multiplikation",
                    test_cases=[
                        ts.TestCase(
                            (
                                ts.Cls(
                                    "CrsMatrix",
                                    val=np.array([1.0, 1.0, 1.0]),
                                    col_idx=np.array([0, 1, 2]),
                                    row_ptr=np.array([0, 1, 2, 3]),
                                ),
                                np.array([-1.5, 0.25, 7.5]),
                            ),
                            np.array([-1.5, 0.25, 7.5]),
                        ),
                        ts.TestCase(
                            (
                                ts.Cls(
                                    "CrsMatrix",
                                    val=np.array([1.0, 1.0, 1.0]),
                                    col_idx=np.array([2, 1, 0]),
                                    row_ptr=np.array([0, 1, 2, 3]),
                                ),
                                np.array([3.5, 11.0, -2.1]),
                            ),
                            np.array([-2.1, 11.0, 3.5]),
                        ),
                        ts.TestCase(
                            (
                                ts.Cls(
                                    "CrsMatrix",
                                    val=np.array([1.0, 1.0, 1.0, -1.0]),
                                    col_idx=np.array([0, 2, 0, 2]),
                                    row_ptr=np.array([0, 2, 2, 4]),
                                ),
                                np.array([7.5, 1031.0, -9.0]),
                            ),
                            np.array([-1.5, 0.0, 16.5]),
                        ),
                    ],
                ),
                ts.Subtask(
                    "c",
                    marks=Fraction(3),
                    function_name="jacobi_step",
                    description="Jacobi-Iterationsschritt",
                    test_cases=[
                        ts.TestCase(
                            (
                                ts.Cls(
                                    "CrsMatrix",
                                    val=np.array([4.0, 1.0, 2.0, -3.0]),
                                    col_idx=np.array([0, 1, 2, 3]),
                                    row_ptr=np.array([0, 1, 2, 3, 4]),
                                ),
                                np.array([1.0, 1.0, 1.0, 1.0]),
                                np.array([0.0, 0.0, 0.0, 0.0]),
                            ),
                            np.array([0.25, 1.0, 0.5, -0.33333333]),
                        ),
                        ts.TestCase(
                            (
                                ts.Cls(
                                    "CrsMatrix",
                                    val=np.array(
                                        [4.0, 2.0, 1.0, -0.5, 2.0, 0.125, -3.0]
                                    ),
                                    col_idx=np.array([0, 1, 1, 2, 2, 3, 3]),
                                    row_ptr=np.array([0, 2, 4, 6, 7]),
                                ),
                                np.array([1.0, 1.0, 1.0, 1.0]),
                                np.array([1.0, 1.0, 1.0, 1.0]),
                            ),
                            np.array([-0.25, 1.5, 0.4375, -0.33333333]),
                        ),
                        ts.TestCase(
                            (
                                ts.Cls(
                                    "CrsMatrix",
                                    val=np.array(
                                        [
                                            8.0,
                                            -1.0,
                                            -2.5,
                                            3.5,
                                            -0.1,
                                            -1.25,
                                            1.0,
                                            0.1,
                                            0.25,
                                        ]
                                    ),
                                    col_idx=np.array([0, 1, 0, 1, 1, 2, 3, 2, 3]),
                                    row_ptr=np.array([0, 2, 4, 7, 9]),
                                ),
                                np.array([1.0, 1.0, 1.0, 1.0]),
                                np.array([1.0, 1.0, 1.0, 1.0]),
                            ),
                            np.array([0.25, 1.0, -0.08, 3.6]),
                        ),
                        ts.TestCase(
                            (
                                ts.Cls(
                                    "CrsMatrix",
                                    val=np.array(
                                        [
                                            -3.4,
                                            0.54,
                                            1.25,
                                            -0.6,
                                            -2.2,
                                            1.25,
                                            2.1,
                                            2.76,
                                            0.3,
                                            -0.3,
                                            -1.96,
                                            -0.94,
                                            0.6,
                                            4.0,
                                            -1.15,
                                            -1.2,
                                        ]
                                    ),
                                    col_idx=np.array(
                                        [0, 2, 1, 3, 2, 4, 0, 3, 5, 1, 4, 6, 2, 5, 3, 6]
                                    ),
                                    row_ptr=np.array([0, 2, 4, 6, 9, 12, 14, 16]),
                                ),
                                np.array([-5.2, 13.4, 0.9, 11.1, -4.15, 0.05, 7.6]),
                                np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]),
                            ),
                            np.array(
                                [
                                    1.68823529,
                                    11.2,
                                    0.15909091,
                                    3.15217391,
                                    1.48469388,
                                    -0.1375,
                                    -7.29166667,
                                ]
                            ),
                        ),
                    ],
                ),
                ts.Subtask(
                    "d",
                    marks=Fraction(3),
                    function_name="sor_step",
                    description="SOR-Iterationsschritt",
                    test_cases=[
                        ts.TestCase(
                            (
                                ts.Cls(
                                    "CrsMatrix",
                                    val=np.array([4.0, 1.0, 2.0, -3.0]),
                                    col_idx=np.array([0, 1, 2, 3]),
                                    row_ptr=np.array([0, 1, 2, 3, 4]),
                                ),
                                np.array([1.0, 1.0, 1.0, 1.0]),
                                np.array([0.25, 1.0, 0.5, -0.33333333]),
                                1.0,
                            ),
                            np.array([0.25, 1.0, 0.5, -0.33333333]),
                        ),
                        ts.TestCase(
                            (
                                ts.Cls(
                                    "CrsMatrix",
                                    val=np.array(
                                        [4.0, 2.0, 1.0, -0.5, 2.0, 0.125, -3.0]
                                    ),
                                    col_idx=np.array([0, 1, 1, 2, 2, 3, 3]),
                                    row_ptr=np.array([0, 2, 4, 6, 7]),
                                ),
                                np.array([1.0, 1.0, 1.0, 1.0]),
                                np.array([-0.25, 1.5, 0.4375, -0.33333333]),
                                1.0,
                            ),
                            np.array([-0.5, 1.21875, 0.52083333, -0.33333333]),
                        ),
                        ts.TestCase(
                            (
                                ts.Cls(
                                    "CrsMatrix",
                                    val=np.array(
                                        [4.0, 2.0, 1.0, -0.5, 2.0, 0.125, -3.0]
                                    ),
                                    col_idx=np.array([0, 0, 1, 1, 2, 2, 3]),
                                    row_ptr=np.array([0, 1, 3, 5, 7]),
                                ),
                                np.array([1.0, 1.0, 1.0, 1.0]),
                                np.array([0.25, 0.5, 0.625, -0.30729167]),
                                1.0,
                            ),
                            np.array([0.25, 0.5, 0.625, -0.30729167]),
                        ),
                        ts.TestCase(
                            (
                                ts.Cls(
                                    "CrsMatrix",
                                    val=np.array(
                                        [
                                            8.0,
                                            -1.0,
                                            -2.5,
                                            3.5,
                                            -0.1,
                                            -1.25,
                                            1.0,
                                            0.1,
                                            0.25,
                                        ]
                                    ),
                                    col_idx=np.array([0, 1, 0, 1, 1, 2, 3, 2, 3]),
                                    row_ptr=np.array([0, 2, 4, 7, 9]),
                                ),
                                np.array([-5.2, 13.4, 0.9, 11.1]),
                                np.array(
                                    [
                                        -1.2875,
                                        3.86339286,
                                        -0.84360714,
                                        66.60616429,
                                    ]
                                ),
                                1.5,
                            ),
                            np.array(
                                [
                                    0.39313616,
                                    4.23237803,
                                    78.76131535,
                                    -13.95987135,
                                ]
                            ),
                        ),
                    ],
                ),
                ts.Subtask(
                    "e",
                    marks=Fraction(3),
                    function_name="cg",
                    description="CG-Verfahren",
                    test_cases=[
                        ts.TestCase(
                            (
                                ts.Cls(
                                    "CrsMatrix",
                                    val=np.array([1.0, 1.0, 1.0]),
                                    col_idx=np.array([0, 1, 2]),
                                    row_ptr=np.array([0, 1, 2, 3]),
                                ),
                                np.array([-1.5, 0.25, 7.5]),
                                np.array([-1.5, 0.25, 7.5]),
                            ),
                            (np.array([-1.5, 0.25, 7.5]), 0),
                        ),
                        ts.TestCase(
                            (
                                ts.Cls(
                                    "CrsMatrix",
                                    val=np.array([1.0, 1.0, 1.0]),
                                    col_idx=np.array([0, 1, 2]),
                                    row_ptr=np.array([0, 1, 2, 3]),
                                ),
                                np.array([-2.75, 0.3, 7.2]),
                                np.array([0.0, 0.0, 0.0]),
                            ),
                            (np.array([-2.75, 0.3, 7.2]), 1),
                        ),
                        ts.TestCase(
                            (
                                ts.Cls(
                                    "CrsMatrix",
                                    val=np.array([3.0, 0.5, 7.0]),
                                    col_idx=np.array([0, 1, 2]),
                                    row_ptr=np.array([0, 1, 2, 3]),
                                ),
                                np.array([6.0, 0.0, 3.0]),
                                np.array([0.0, 0.0, 0.0]),
                            ),
                            (np.array([2.0, 0.0, 3.0 / 7.0]), 2),
                        ),
                        ts.TestCase(
                            (
                                ts.Cls(
                                    "CrsMatrix",
                                    val=np.array([2.0, -1.0, 3.0, 0.5, 1.0, -0.5, 2.0]),
                                    col_idx=np.array([0, 0, 1, 1, 2, 2, 3]),
                                    row_ptr=np.array([0, 1, 3, 5, 7]),
                                ),
                                np.array([0.0, -12.0, -3.0, 3.0 / 2.0]),
                                np.array([0.0, 0.0, 0.0, 0.0]),
                            ),
                            (np.array([0.0, -4.0, -1.0, 1.0 / 2.0]), 1),
                        ),
                    ],
                ),
            ],
        ),
        ts.Task(
            2,
            "poisson",
            "Poisson-Randwertproblem",
            allowed_imports={"numpy", "sparse_linalg"},
            subtasks=[
                ts.Subtask(
                    "a",
                    marks=Fraction(3),
                    function_name="assemble_poisson_matrix",
                    description="Systemmatrix aufstellen",
                    test_cases=[
                        ts.TestCase(
                            (3,),
                            ts.Cls(
                                "CrsMatrix",
                                val=np.array([16.0]),
                                col_idx=np.array([0]),
                                row_ptr=np.array([0, 1]),
                            ),
                        ),
                        ts.TestCase(
                            (4,),
                            ts.Cls(
                                "CrsMatrix",
                                val=np.array(
                                    [
                                        36.0,
                                        -9.0,
                                        -9.0,
                                        -9.0,
                                        36.0,
                                        -9.0,
                                        -9.0,
                                        36.0,
                                        -9.0,
                                        -9.0,
                                        -9.0,
                                        36.0,
                                    ]
                                ),
                                col_idx=np.array([0, 1, 2, 0, 1, 3, 0, 2, 3, 1, 2, 3]),
                                row_ptr=np.array([0, 3, 6, 9, 12]),
                            ),
                        ),
                        ts.TestCase(
                            (6,),
                            ts.Cls(
                                "CrsMatrix",
                                val=np.array(
                                    [
                                        100.0,
                                        -25.0,
                                        -25.0,
                                        -25.0,
                                        100.0,
                                        -25.0,
                                        -25.0,
                                        -25.0,
                                        100.0,
                                        -25.0,
                                        -25.0,
                                        -25.0,
                                        100.0,
                                        -25.0,
                                        -25.0,
                                        100.0,
                                        -25.0,
                                        -25.0,
                                        -25.0,
                                        -25.0,
                                        100.0,
                                        -25.0,
                                        -25.0,
                                        -25.0,
                                        -25.0,
                                        100.0,
                                        -25.0,
                                        -25.0,
                                        -25.0,
                                        -25.0,
                                        100.0,
                                        -25.0,
                                        -25.0,
                                        100.0,
                                        -25.0,
                                        -25.0,
                                        -25.0,
                                        -25.0,
                                        100.0,
                                        -25.0,
                                        -25.0,
                                        -25.0,
                                        -25.0,
                                        100.0,
                                        -25.0,
                                        -25.0,
                                        -25.0,
                                        -25.0,
                                        100.0,
                                        -25.0,
                                        -25.0,
                                        100.0,
                                        -25.0,
                                        -25.0,
                                        -25.0,
                                        100.0,
                                        -25.0,
                                        -25.0,
                                        -25.0,
                                        100.0,
                                        -25.0,
                                        -25.0,
                                        -25.0,
                                        100.0,
                                    ]
                                ),
                                col_idx=np.array(
                                    [
                                        0,
                                        1,
                                        4,
                                        0,
                                        1,
                                        2,
                                        5,
                                        1,
                                        2,
                                        3,
                                        6,
                                        2,
                                        3,
                                        7,
                                        0,
                                        4,
                                        5,
                                        8,
                                        1,
                                        4,
                                        5,
                                        6,
                                        9,
                                        2,
                                        5,
                                        6,
                                        7,
                                        10,
                                        3,
                                        6,
                                        7,
                                        11,
                                        4,
                                        8,
                                        9,
                                        12,
                                        5,
                                        8,
                                        9,
                                        10,
                                        13,
                                        6,
                                        9,
                                        10,
                                        11,
                                        14,
                                        7,
                                        10,
                                        11,
                                        15,
                                        8,
                                        12,
                                        13,
                                        9,
                                        12,
                                        13,
                                        14,
                                        10,
                                        13,
                                        14,
                                        15,
                                        11,
                                        14,
                                        15,
                                    ]
                                ),
                                row_ptr=np.array(
                                    [
                                        0,
                                        3,
                                        7,
                                        11,
                                        14,
                                        18,
                                        23,
                                        28,
                                        32,
                                        36,
                                        41,
                                        46,
                                        50,
                                        53,
                                        57,
                                        61,
                                        64,
                                    ]
                                ),
                            ),
                        ),
                    ],
                ),
                ts.Subtask(
                    "b",
                    marks=Fraction(2),
                    function_name="assemble_rhs",
                    description="Rechte Seite aufstellen",
                    test_cases=[
                        ts.TestCase((3, c0, c0), np.array([0.0])),
                        ts.TestCase((4, c0, discont1), np.array([0.0, 9.0, 0.0, 9.0])),
                        ts.TestCase(
                            (5, c0, lin_y),
                            np.array([4.0, 0.0, 4.0, 8.0, 0.0, 8.0, 28.0, 16.0, 28.0]),
                        ),
                        ts.TestCase(
                            (5, c10, lin_y),
                            np.array(
                                [14.0, 10.0, 14.0, 18.0, 10.0, 18.0, 38.0, 26.0, 38.0]
                            ),
                        ),
                        ts.TestCase(
                            (5, m6x, x_cubed),
                            np.array(
                                [
                                    -1.25,
                                    -1.0,
                                    18.25,
                                    -1.5,
                                    -3.0,
                                    11.5,
                                    -1.25,
                                    -1.0,
                                    18.25,
                                ]
                            ),
                        ),
                    ],
                ),
                ts.Subtask(
                    "c",
                    marks=Fraction(3),
                    function_name="solve_poisson",
                    description="Poisson-Problem lösen",
                    test_cases=[
                        ts.TestCase((5, c0, c0), np.zeros((5, 5), dtype=float)),
                        ts.TestCase((5, c0, cm1), -np.ones((5, 5), dtype=float)),
                        ts.TestCase(
                            (5, c0, x_half),
                            np.array(
                                [
                                    [0.0, 0.125, 0.25, 0.375, 0.5],
                                    [0.0, 0.125, 0.25, 0.375, 0.5],
                                    [0.0, 0.125, 0.25, 0.375, 0.5],
                                    [0.0, 0.125, 0.25, 0.375, 0.5],
                                    [0.0, 0.125, 0.25, 0.375, 0.5],
                                ]
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
