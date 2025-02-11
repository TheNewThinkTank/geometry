"""_summary_
"""

import math


def arbitrary_triangle_area(a, b, c):
    return .5 * math.sqrt(a ** 2 * c ** 2 - ((a ** 2 + c ** 2 - b ** 2) / 2) ** 2)


def inscribed_circle_radius(a, b, c, T):
    return 2 * T / (a + b + c)


def inscribed_circle_area(r):
    return math.pi * r ** 2


a = 3
b = 4
c = 5

# print(arbitrary_triangle_area(a, b, c))
# print(inscribed_circle_radius(a, b, c, 6.0))

print(inscribed_circle_area(1.0))

# inscribed_circle_area(
#     inscribed_circle_radius(a, b, c, arbitrary_triangle_area(a, b, c))
#                       )
