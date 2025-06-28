import pathlib
from fractions import Fraction
import numpy as np
import testsuite as ts


sheet = ts.Sheet(
    7,
    tasks=[
        ts.Task(
            1,
            "bezier",
            description="Bezierkurven",
            allowed_imports={"numpy"},
            subtasks=[
                ts.Subtask(
                    "a",
                    marks=Fraction(2),
                    function_name="de_casteljau_step",
                    description="De Casteljau-Schritt",
                    test_cases=[
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 0.0]]), 0.5),
                            np.array([[0.5, 0]]),
                        ),
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 0.0]]), 0.2),
                            np.array([[0.2, 0]]),
                        ),
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 1.0]]), 0.5),
                            np.array([[0.5, 0.5]]),
                        ),
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 1.0]]), 0.2),
                            np.array([[0.2, 0.2]]),
                        ),
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 1.0], [2.0, 2.0]]), 0.5),
                            np.array([[0.5, 0.5], [1.5, 1.5]]),
                        ),
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 1.0], [2.0, 0.0]]), 0.5),
                            np.array([[0.5, 0.5], [1.5, 0.5]]),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [[0.0, 0.0], [1.0, 1.0], [2.0, 2.0], [3.0, 3.0]]
                                ),
                                0.2,
                            ),
                            np.array([[0.2, 0.2], [1.2, 1.2], [2.2, 2.2]]),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [[3.0, 2.0], [2.0, 5.0], [7.0, 6.0], [8.0, 1.0]]
                                ),
                                0.3,
                            ),
                            np.array([[2.7, 2.9], [3.5, 5.3], [7.3, 4.5]]),
                        ),
                    ],
                ),
                ts.Subtask(
                    "b",
                    marks=Fraction(2),
                    function_name="de_casteljau",
                    description="De Casteljau",
                    test_cases=[
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 0.0]]), 0.5),
                            np.array([0.5, 0]),
                        ),
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 0.0]]), 0.2),
                            np.array([0.2, 0]),
                        ),
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 1.0]]), 0.2),
                            np.array([0.2, 0.2]),
                        ),
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 1.0], [2.0, 2.0]]), 0.5),
                            np.array([1.0, 1.0]),
                        ),
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 1.0], [2.0, 0.0]]), 0.5),
                            np.array([1.0, 0.5]),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [[0.0, 0.0], [1.0, 1.0], [2.0, 2.0], [3.0, 3.0]]
                                ),
                                0.5,
                            ),
                            np.array([1.5, 1.5]),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [[0.0, 0.0], [1.0, 1.0], [2.0, 2.0], [3.0, 3.0]]
                                ),
                                0.2,
                            ),
                            np.array([0.6, 0.6]),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [
                                        [0.0, 0.0],
                                        [1.0, 1.0],
                                        [2.0, 2.0],
                                        [3.0, 3.0],
                                        [4.0, 4.0],
                                    ]
                                ),
                                0.2,
                            ),
                            np.array([0.8, 0.8]),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [
                                        [0.0, 0.0],
                                        [1.0, 1.0],
                                        [2.0, 2.0],
                                        [1.0, 1.0],
                                        [0.0, 0.0],
                                    ]
                                ),
                                0.5,
                            ),
                            np.array([1.25, 1.25]),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [[3.0, 2.0], [2.0, 5.0], [7.0, 6.0], [8.0, 1.0]]
                                ),
                                0.3,
                            ),
                            np.array([3.45, 4.052]),
                        ),
                    ],
                ),
                ts.Subtask(
                    "c",
                    marks=Fraction(2),
                    function_name="bezier1",
                    description="Bézierkurve approximieren",
                    test_cases=[
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 0.0]]), 2),
                            np.array([[0.0, 0.0], [1.0, 0.0]]),
                        ),
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 1.0]]), 2),
                            np.array([[0.0, 0.0], [1.0, 1.0]]),
                        ),
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 0.0]]), 3),
                            np.array([[0.0, 0.0], [0.5, 0.0], [1.0, 0.0]]),
                        ),
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 1.0]]), 3),
                            np.array([[0.0, 0.0], [0.5, 0.5], [1.0, 1.0]]),
                        ),
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 1.0], [2.0, 0.0]]), 2),
                            np.array([[0.0, 0.0], [2.0, 0.0]]),
                        ),
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 1.0], [2.0, 0.0]]), 3),
                            np.array([[0.0, 0.0], [1.0, 0.5], [2.0, 0.0]]),
                        ),
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 1.0], [2.0, 0.0]]), 5),
                            np.array(
                                [
                                    [0.0, 0.0],
                                    [0.5, 0.375],
                                    [1.0, 0.5],
                                    [1.5, 0.375],
                                    [2.0, 0.0],
                                ]
                            ),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [[3.0, 2.0], [2.0, 5.0], [7.0, 6.0], [8.0, 1.0]]
                                ),
                                3,
                            ),
                            np.array([[3.0, 2.0], [4.75, 4.5], [8.0, 1.0]]),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [[3.0, 2.0], [3.04, 3.528], [4.0, 6.0], [8.0, 1.0]]
                                ),
                                10,
                            ),
                            np.array(
                                [
                                    [3.0, 2.0],
                                    [3.0503155, 2.53275171],
                                    [3.18622771, 3.06616187],
                                    [3.42518519, 3.53096296],
                                    [3.78463649, 3.85788752],
                                    [4.28203018, 3.97766804],
                                    [4.93481481, 3.82103704],
                                    [5.76043896, 3.31872702],
                                    [6.77635117, 2.40147051],
                                    [8.0, 1.0],
                                ]
                            ),
                        ),
                    ],
                ),
                ts.Subtask(
                    "d",
                    marks=Fraction(2),
                    function_name="add_control_point",
                    description="Kontrollpunkte hinzufügen",
                    test_cases=[
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 0.0]]),),
                            np.array([[0.0, 0.0], [0.5, 0.0], [1.0, 0.0]]),
                        ),
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [0.5, 0.0], [1.0, 0.0]]),),
                            np.array(
                                [[0.0, 0.0], [1 / 3, 0.0], [2 / 3, 0.0], [1.0, 0.0]]
                            ),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [[0.0, 0.0], [1 / 3, 0.0], [2 / 3, 0.0], [1.0, 0.0]]
                                ),
                            ),
                            np.array(
                                [
                                    [0.0, 0.0],
                                    [0.25, 0.0],
                                    [0.5, 0.0],
                                    [0.75, 0.0],
                                    [1.0, 0.0],
                                ]
                            ),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [[0.0, 0.0], [1 / 3, 1.0], [2 / 3, 2.0], [1.0, 3.0]]
                                ),
                            ),
                            np.array(
                                [
                                    [0.0, 0.0],
                                    [0.25, 0.75],
                                    [0.5, 1.5],
                                    [0.75, 2.25],
                                    [1.0, 3.0],
                                ]
                            ),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [[3.0, 2.0], [2.0, 5.0], [7.0, 6.0], [8.0, 1.0]]
                                ),
                            ),
                            np.array(
                                [
                                    [3.0, 2.0],
                                    [2.25, 4.25],
                                    [4.5, 5.5],
                                    [7.25, 4.75],
                                    [8.0, 1.0],
                                ]
                            ),
                        ),
                    ],
                ),
                ts.Subtask(
                    "e",
                    marks=Fraction(2),
                    function_name="split_curve",
                    description="Bézierkurve aufteilen",
                    test_cases=[
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 0.0]]),),
                            (
                                np.array([[0.0, 0.0], [0.5, 0.0]]),
                                np.array([[0.5, 0.0], [1.0, 0.0]]),
                            ),
                        ),
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 1.0]]),),
                            (
                                np.array([[0.0, 0.0], [0.5, 0.5]]),
                                np.array([[0.5, 0.5], [1.0, 1.0]]),
                            ),
                        ),
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 1.0], [2.0, 0.0]]),),
                            (
                                np.array([[0.0, 0.0], [0.5, 0.5], [1.0, 0.5]]),
                                np.array([[1.0, 0.5], [1.5, 0.5], [2.0, 0.0]]),
                            ),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [[3.0, 2.0], [2.0, 5.0], [7.0, 6.0], [8.0, 1.0]]
                                ),
                            ),
                            (
                                np.array(
                                    [[3.0, 2.0], [2.5, 3.5], [3.5, 4.5], [4.75, 4.5]]
                                ),
                                np.array(
                                    [[4.75, 4.5], [6.0, 4.5], [7.5, 3.5], [8.0, 1.0]]
                                ),
                            ),
                        ),
                    ],
                ),
                ts.Subtask(
                    "f",
                    marks=Fraction(2),
                    function_name="bezier2",
                    description="Bézierkurven rekursiv approximieren",
                    test_cases=[
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 0.0]]), 0),
                            np.array([[0.0, 0.0], [1.0, 0.0]]),
                        ),
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 0.0]]), 1),
                            np.array([[0.0, 0.0], [0.5, 0.0], [1.0, 0.0]]),
                        ),
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 0.0]]), 2),
                            np.array(
                                [
                                    [0.0, 0.0],
                                    [0.25, 0.0],
                                    [0.5, 0.0],
                                    [0.75, 0.0],
                                    [1.0, 0.0],
                                ]
                            ),
                        ),
                        ts.TestCase(
                            (np.array([[0.0, 0.0], [1.0, 0.0]]), 3),
                            np.array(
                                [
                                    [0.0, 0.0],
                                    [0.125, 0.0],
                                    [0.25, 0.0],
                                    [0.375, 0.0],
                                    [0.5, 0.0],
                                    [0.625, 0.0],
                                    [0.75, 0.0],
                                    [0.875, 0.0],
                                    [1.0, 0.0],
                                ]
                            ),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [[3.0, 2.0], [2.0, 5.0], [6.0, 6.0], [8.0, 1.0]]
                                ),
                                1,
                            ),
                            np.array(
                                [
                                    [3.0, 2.0],
                                    [2.5, 3.5],
                                    [3.25, 4.5],
                                    [4.375, 4.5],
                                    [5.5, 4.5],
                                    [7.0, 3.5],
                                    [8.0, 1.0],
                                ]
                            ),
                        ),
                        ts.TestCase(
                            (
                                np.array(
                                    [[3.0, 2.0], [2.0, 5.0], [6.0, 6.0], [8.0, 1.0]]
                                ),
                                2,
                            ),
                            np.array(
                                [
                                    [3.0, 2.0],
                                    [2.75, 2.75],
                                    [2.8125, 3.375],
                                    [3.078125, 3.8125],
                                    [3.34375, 4.25],
                                    [3.8125, 4.5],
                                    [4.375, 4.5],
                                    [4.9375, 4.5],
                                    [5.59375, 4.25],
                                    [6.234375, 3.6875],
                                    [6.875, 3.125],
                                    [7.5, 2.25],
                                    [8.0, 1.0],
                                ]
                            ),
                        ),
                    ],
                ),
            ],
        ),
        ts.Task(
            2,
            "interpolation",
            description="Polynominterpolation",
            allowed_imports={"numpy", "numpy.linalg"},
            subtasks=[
                ts.Subtask(
                    "a",
                    marks=Fraction(2),
                    function_name="interpolate_linearly",
                    description="Polynome in Python",
                    test_cases=[
                        ts.TestCase(([0.0, 0.0], [1.0, 0.0]), np.poly1d([0.0, 0.0])),
                        ts.TestCase(([0.0, 0.0], [1.0, 1.0]), np.poly1d([1.0, 0.0])),
                        ts.TestCase(([0.0, 0.0], [1.0, 2.0]), np.poly1d([2.0, 0.0])),
                        ts.TestCase(([1.0, 0.0], [2.0, 1.0]), np.poly1d([1.0, -1.0])),
                        ts.TestCase(([1.0, 1.0], [3.0, 1.0]), np.poly1d([0.0, 1.0])),
                        ts.TestCase(
                            ([-2.0, 1.0], [-3.0, 2.0]), np.poly1d([-1.0, -1.0])
                        ),
                        ts.TestCase(
                            ([-8.0, -6.0], [-3.0, 4.0]), np.poly1d([2.0, 10.0])
                        ),
                    ],
                ),
                ts.Subtask(
                    "b",
                    marks=Fraction(2),
                    function_name="newton_matrix",
                    description="Newton-Matrix",
                    test_cases=[
                        ts.TestCase((np.array([]),), np.zeros((0, 0))),
                        ts.TestCase(
                            (np.array([0.0, 1.0]),), np.array([[1.0, 0.0], [1.0, 1.0]])
                        ),
                        ts.TestCase(
                            (np.array([-2.0, 0.0, 2.0]),),
                            np.array(
                                [[1.0, 0.0, 0.0], [1.0, 2.0, 0.0], [1.0, 4.0, 8.0]]
                            ),
                        ),
                        ts.TestCase(
                            (np.array([-2.0, 0.5, 1.5]),),
                            np.array(
                                [[1.0, 0.0, 0.0], [1.0, 2.5, 0.0], [1.0, 3.5, 3.5]]
                            ),
                        ),
                    ],
                ),
                ts.Subtask(
                    "c",
                    marks=Fraction(2),
                    function_name="newton_polynomial",
                    description="Newton-Polynom",
                    test_cases=[
                        ts.TestCase((np.array([]), np.array([])), np.poly1d([])),
                        ts.TestCase(
                            (np.array([1.0, 1.0]), np.array([0.0, 1.0])),
                            np.poly1d([1.0, 1.0]),
                        ),
                        ts.TestCase(
                            (np.array([1.0, 2.0, 3.0]), np.array([0.0, 1.0, 1.0])),
                            np.poly1d([3.0, -1.0, 1.0]),
                        ),
                    ],
                ),
                ts.Subtask(
                    "d",
                    marks=Fraction(2),
                    function_name="interpolating_polynomial",
                    description="Newton-Interpolation",
                    test_cases=[
                        ts.TestCase((np.array([]), np.array([])), np.poly1d([])),
                        ts.TestCase(
                            (np.array([1.0, 2.0, 3.0]), np.array([1.0, 1.0, 1.0])),
                            np.poly1d([1]),
                        ),
                        ts.TestCase(
                            (np.array([1.0, 2.0, 3.0]), np.array([0.0, 2.0, 1.0])),
                            np.poly1d([-1.5, 6.5, -5.0]),
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
