"""getFields.py
returns: float
"""

import math


__author__ = 'johnp80'
__email__ = 'johnp90380@gmail.com'


def get_fields(start_x, start_y, end_x, end_y):
    """ return type float

    :param end_y: ending  coordinates(y)
    :param end_x: ending coordinates(x)
    :param start_y: starting  coordinates(y)
    :param start_x: starting  coordinates(x)
    """

    fields = round(
        math.sqrt(
            (math.pow((end_x - start_x), 2) + math.pow((end_y - start_y), 2))),
        2)
    return fields










