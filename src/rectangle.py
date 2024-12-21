
"""
Module rectangle
================
This module supplies five functions,

rectangle_slopes(radians) to calculate the 4 slopes of a rectangle,
tilted from the horizontal axis,
by an angle given in radians.

intersect(a, x, y) to calculate the intersection,
of each rectangles side with the vertical axis,
given the slope and one point on each line.

find_point_on_line(a, b, d, m) to calculate nearest point,
on each rectangles side (given by slope m),
with respect to a known point with coordinates (a, b), at a distance d.

transform_rectangle(i, ec, height, coords=[0, 0], width=30),
to rotate rectangle by a certain angle wrt. horizontal.

add_circle(j, arr, x, xC, y, yC, c, z) to add a circular patch to a given figure.
"""

import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def rectangle_slopes(radians: float) -> tuple:
    """Function to calculate the 4 slopes of a rectangle.
    First import, and then use, for example:

    >>> from rectangle import rectangle_slopes
    >>> rectangle_slopes(math.radians(70))
    (2.747477419454621, 2.747477419454621, -0.3639702342662024, -0.3639702342662024)

    :param radians: Angle to calculate the slopes from
    :type radians: float
    :return: The 4 calculated slopes
    :rtype: float
    """
    
    a1, a3 = np.tan(radians), np.tan(radians - math.radians(90))
    # a2, a4 = a1, a3
    return (a1, a1, a3, a3)


def intersect(a: float, x: float, y: float) -> float:
    '''Intersection of straight line with y-axis.'''

    return y - a * x


def find_point_on_line(a: float, b: float, d: float, m: float) -> tuple:
  '''Find new point on straight line with slope m, with a known point (a, b),
  at a distance to that point, d.'''

  k: float = d / np.sqrt(1 + m ** 2)
  x: float = a + k
  y: float = b + k * m
  return (x, y)


def transform_rectangle(degrees: float,
                        i: int,
                        ec: str,
                        height: float,
                        coords: list=[0, 0],
                        width: float=30
                        ):
    '''Transform rectangle.'''

    ts = eval("ax{i}.transData")
    tr = mpl.transforms.Affine2D().rotate_deg_around(coords[0], coords[1],
                                                     degrees)
    t = tr + ts
    mpl.patches.Rectangle((coords[0], coords[1]), width, height,
                                  linewidth=1, edgecolor=ec, facecolor='none',
                                  transform=t)
    exec("ax{i}.add_patch(rect)")


def add_circle(j: int, arr, x, xC, y, yC, c: str, z: int):
    '''Add a circular patch to figure.'''

    for i in range(len(arr)):
        plt.Circle((x[i] - xC, y[i] - yC), radius=arr[i], color=c,
                          fill=False, zorder=z)
        exec("ax{j}.add_patch(circ)")


def main():
    degrees: float = 70
    print(f'{rectangle_slopes(math.radians(degrees))= }')
    print(f'{intersect(.5, 3, 12)= }')
    print(f'{find_point_on_line(1, 1, 5, .5)= }')  


if __name__ == '__main__':
    main()
