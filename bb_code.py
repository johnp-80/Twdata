__author__ = 'johnp80'


def make_coords(x_coord, y_coord):
    coords = str(x_coord) + "|" + str(y_coord)
    return coords


def print_claim(coords):
    start_tag = "[claim]"
    end_tag = "[/claim]"
    print "{}{}{}".format(start_tag, coords, end_tag)


def print_coord(coords):
    start_tag = "[coord]"
    end_tag = "[/coord]"
    print "{}{}{}".format(start_tag, coords, end_tag)


def print_player(player_name):
    start_tag = "[player]"
    end_tag = "[/player]"
    print "{}{}{}".format(start_tag, player_name, end_tag)


def print_code_tag(coords):
    start_tag = "[code]"
    end_tag = "[/code]"
    print "{}".format(start_tag)
    for coord in coords:
        print "{} ".format(coord)
    print "{}".format(end_tag)


def print_open_table_header(*args):
    start_tag = "[table]"
    column_start = "[**]"
    column_end = "[/**]"
    column_divider = "[||]"
    print "{}\n{}".format(start_tag, column_start)
    for arg in args:
        print "{} {}".format(arg, column_divider)
    print "{}".format(column_end)


def print_close_table():
    print "[/table]"


def print_table_rows(*args):
    row_start = "[*]"
    row_divider = "[|]"
    last_row = len(*args)
    for x in args:
        if args > 1:
            if last_row == x:
                print "{}{}".format(row_start, x)
            else:
                print "{}{}{}".format(row_start, x, row_divider)
        else:
            print "{}{}".format(row_start, x)
