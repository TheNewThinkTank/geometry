
import math
from typing import Final
import numpy as np
from geometry.rectangle import (  # type: ignore
    rectangle_slopes,
    intersect,
    find_point_on_line,
)


def test_rectangle_slopes():
    angle: Final = math.radians(70)
    expected_slopes = np.array([
        2.747477419454621,
        2.747477419454621,
        -0.36397023426620245,
        -0.36397023426620245,
    ])
    actual_slopes = np.array(rectangle_slopes(angle))

    assert np.allclose(actual_slopes, expected_slopes, atol=1e-9), "Slopes do not match"



def test_intersect():
    intersection: int = 10.5
    assert intersect(0.5, 3, 12) == intersection, f"Should be {intersection}"


def test_find_point_on_line():
    point_on_line: tuple = (5.47213595499958, 3.23606797749979)
    assert (
        find_point_on_line(1, 1, 5, 0.5) == point_on_line
    ), f"Should be {point_on_line}"
