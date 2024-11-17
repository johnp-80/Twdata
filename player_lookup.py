__author__ = 'johnp80'

import sys

from database import Db


def player_lookup(player):
    """
    :param player:
    :return: list
    """
    tw_db = Db()
    result = tw_db.sp_db_query("findPlayer", player)

    return result


def player_print(player):
    """

    :param player:
    :return:NONE
    """
    result = player_lookup(player)
    for row in result:
        print row


def main(*args):
    """Queries the database for a player name, returns player information.
    :param args: optional, player name to lookup. If no name is provided,
    script will prompt for a name.
    """
    data = []
    if len(sys.argv) > 1:
        data = player_lookup(sys.argv[1])
    elif len(args) == 0:
        player = raw_input("Player name to lookup: ")
        data = player_lookup(player)
    else:
        data = player_lookup(args)

    print data


if __name__ == "__main__":
    main()

