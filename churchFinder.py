"""churchFinder.py
Attempts to find the optimal church placement.

"""

import csv

import getFields
import get_villages

__author__ = 'johnp80'
__email__ = 'johnp90380'


class Village:
    """

    :param v_id: village id
    :param v_name: village name
    :param player: player id
    :param x: x coordinate
    :param y: y coordinate
    :param points: village points
    :param rank: village type
    :param covered: number of villages covered
    :param villages: a list of villages that would be covered by the church
    """

    def __init__(self, v_id, v_name, player,
                 x, y, points, rank, covered=0, villages=[]):
        self.v_id = v_id
        self.name = v_name
        self.player = player
        self.x = x
        self.y = y
        self.points = points
        self.rank = rank
        self.covered = covered
        self.villages = villages

    def __repr__(self):
        return repr((int(self.v_id), self.name, int(self.x), int(self.y),
                     int(self.points), int(self.rank), self.covered))


v_list = list(get_villages.get_villages('fratibus'))
c_list = []


class ChurchCoverage(Village):
    """

    :param c_village_x:
    :param c_village_y:
    :param v_id:
    :param v_name:
    :param player:
    :param x:
    :param y:
    :param points:
    :param continent:
    """

    def __init__(self, c_village_x, c_village_y, v_id, v_name, player, x, y,
                 points, rank):
        Village.__init__(self, v_id, v_name, player, x, y, points, rank)
        self.c_villageX = c_village_x
        self.c_villageY = c_village_y
        self.c_village = str(c_village_x + '|' + c_village_y)
        self.covered_list = []

    def __repr__(self):
        return repr((self.c_village, self.covered_list))

    def __str__(self):
        if len(self.covered_list) > 0:
            return "{:<7} :| {:>}\n".format(self.c_village, self.covered_list)
        else:
            return "{:<}  None\n".format(self.c_village)

    def covered_villages(self, x, y):
        """

        :param x:
        :param y:
        """
        self.covered_list.append(str(x + '|' + y))

    def get_villages(self, c_list):

        """

        :param c_list:
        """
        for x in xrange(0, len(c_list)):
            if getFields.get_fields(int(self.c_villageX), int(self.c_villageY),
                                    int(c_list[x].x), int(c_list[x].y)) < 8.00:
                self.covered_villages(c_list[x].x, c_list[x].y)


def church_zone(start_x, start_y, villages, fields_to_cover):

    """return type list

    :param start_x: village starting coordinates (x)
    :param start_y: village starting coordinates (y)
    :param villages: a list of villages
    :param fields_to_cover: church radius(or zone where op is being conducted)
    """

    church_villages = []  # villages in the designated church radius
    results = []
    for village in xrange(0, len(villages[0])):
        end_x = villages[0][village]
        end_y = villages[0][village]
        result = getFields.get_fields(int(start_x), int(start_y),
                                      int(end_x),
                                      int(end_y))
        results.append(result)
        church_villages.append((end_x, end_y))

    v_remove = []
    for v in xrange(0, len(church_villages)):
        # removes villages that are outside the church radius
        if results[v] > fields_to_cover:
            v_remove.append((church_villages[v]))

    for x in xrange(0, len(v_remove)):
        church_villages.remove(v_remove[x])

    for x in xrange(0, len(church_villages)):

        temp_str = (
            str(church_villages[x][0]) + '|' + str(church_villages[x][1]))
        church_villages[x] = temp_str
        # Checks to see if the village listed is the church
        if int(church_villages[x][0]) == start_x and int(
                church_villages[x][1]) == start_y:
            church_villages.remove(church_villages[x])

    return church_villages


for x in xrange(0, len(v_list)):
    c_list.append(
        Village(v_list[x][0], v_list[x][1], v_list[x][2], v_list[x][3],
                v_list[x][4], v_list[x][5], v_list[x][6]))

for x in xrange(0, len(v_list)):
    count = 0
    churches = []
    for y in xrange(1, len(v_list)):
        d = getFields.get_fields(int(v_list[x][3]), int(v_list[x][4]),
                                 int(v_list[y][3]), int(v_list[y][4]))
        if d < 8.0:
            churches.append((v_list[y][3], v_list[y][4]))
            count += 1
    result = church_zone(v_list[x][3], v_list[x][4], churches, 8)
    c_list[x].covered = count
    c_list[x].villages.append(result)


new_list = sorted(c_list, key=lambda village: village.covered, reverse=True)

with open('churches.txt', 'w') as w:
    for row in new_list:
        w.write(str(row) + '\n')
w.close()
print new_list



