import getFields
import get_villages
import find_churches


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
        end_x = int(villages[0][village][0:3])
        end_y = int(villages[0][village][4:7])
        result = getFields.get_fields(int(start_x), int(start_y), int(end_x),
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


def lookup_player():
    player_name = raw_input("enter the players name")
    return player_name


def get_coverage():
    player = lookup_player()
    # Calls find_churches.py, with the input, output, and the format desired.
    churches = [
        find_churches.get_churches("reports.txt", "chr_churches.txt", 1)]
    one_church = 4.00
    two_church = 6.00
    three_church = 8.00

    villages = [get_villages.get_villages(player_name)]

    v = []
    for village in xrange(0, len(churches[0])):
        church_level = int(churches[0][village][1])
        start_x = int(churches[0][village][0][0:3])
        start_y = int(churches[0][village][0][4:7])

        if church_level == 1:
            church = 4.00

        elif church_level == 2:
            church = 6.00
        else:
            church = 8.00

        result = church_zone(start_x, start_y, villages, church)
        v.append(result)

    for village in xrange(0, len(churches[0])):
        print "[*][coord]{}|{}[/coord][|]{}[|] ".format(
            churches[0][village][0][0:3], churches[0][village][0][4:7],
            churches[0][village][1])
        for x in xrange(0, len(v[village])):
            print " {}".format(v[village][x])


def main():
    get_coverage()


if __name__ == '__main__':
    main()
