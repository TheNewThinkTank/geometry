
from geometry.trigonometry import (  # type: ignore
    arbitrary_triangle_area,
    inscribed_circle_radius,
    inscribed_circle_area
)


def test_arbitrary_triangle_area():
    assert arbitrary_triangle_area(3, 4, 5) == 6.0


def test_inscribed_circle_radius():
    assert inscribed_circle_radius(3, 4, 5, 6.0) == 1.0


def test_inscribed_circle_area():
    assert inscribed_circle_area(1.0) == 3.141592653589793
