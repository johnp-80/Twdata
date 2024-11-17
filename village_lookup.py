__author__ = 'johnp80'

import re
import sys

from database import Db


def village_lookup(x_coord='500', y_coord='500'):
    """Returns information about a village.

    """

    query = "findVillage"
    # cnx = MySQLdb.Connect(db.cnx_params['host'],
    # db.cnx_params['user'],
    #                       db.cnx_params['pwd'],
    #                       db.cnx_params['server'])
    # cursor = cnx.cursor()
    # cursor.callproc(query, (x_coord, y_coord))
    # results = cursor.fetchall()
    twdb = Db()
    results = twdb.sp_db_query(query, x_coord, y_coord)
    return list(results)


def get_coords():
    """
    Gets the coordinates if none are provided


    :rtype : int,int
    """
    coords = raw_input("Please enter the coords")
    coords_search = re.compile('(\d{1,3})(\||,|\s)(\d{1,3})')
    user_input = re.match(coords_search, coords)
    x_coord = ''
    y_coord = ''
    if user_input:
        x_coord = user_input.group(1)
        y_coord = user_input.group(3)
    return x_coord, y_coord


def main(*args):
    """
    prints out the village information
    :rtype : None
    :param x_coord: x coordinate on the map
    :param y_coord: y coordinate on the map
    """
    x_coord = 0
    y_coord = 0
    if len(sys.argv) <= 1:
        if len(args) == 0:
            coords = get_coords()
            x_coord = coords[0]
            y_coord = coords[1]
        elif len(args) == 1:
            simple_coord = re.compile('(\d{1,3})(\||,\s)(\d{1,3})')
            v_coords = re.match(simple_coord, str(args))
            x_coord = v_coords.group(1)
            y_coord = v_coords.group(3)
        elif len(args) == 2:
            x_coord = args[0]
            y_coord = args[1]

    elif len(sys.argv) == 2:

        simple_coord = re.compile('(\d{1,3})(\||,|\w)(\d{1,3})')
        tmp_coords = re.match(simple_coord, str(sys.argv[1]))
        x_coord = tmp_coords.group(1)
        y_coord = tmp_coords.group(3)

    elif len(sys.argv) == 3:
        x_coord = sys.argv[1]
        y_coord = sys.argv[2]

    else:
        print "usage village_lookup.py 500|500 or 500 500, or 500,500"

    results = village_lookup(x_coord, y_coord)
    if (len(results)) == 0:
        print "No Results found for {0}|{1}".format(x_coord, y_coord)
    else:
        info = ['village name', 'village points', 'player name',
                'player points', 'tribe name', 'tribe tag']
        for row in xrange(0, len(results)):
            print "{}:{}\n".format(info[row], results[row])


if __name__ == "__main__":
    main()
