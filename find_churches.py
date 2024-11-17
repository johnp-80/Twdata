"""Finds the churches out of a list of reports"""

import re
import os
import os.path

import twdataerror

__author__ = 'johnp80'
__email__ = 'johnp90380'


def get_churches(reports, ch_info, output_info=0):
    """  Finds churches by finding church levels indicated in report titles.
        :param reports: a text file of report titles
        :param ch_info: location of church information
        :param output_info: type of output desired default is to print to a file
    """

    coords = re.compile(
        ur'\[\d{3}\s([\w\W\d\s]{0,33}\s)?\((\d{3}\|\d{3})\)\sK\d\d\]',
        re.MULTILINE)
    church_level = re.compile(ur'Church:\s(\?|1|2|3)', re.MULTILINE)
    report_text = ''
    report_path = r"" #Your directory path goes here. 
    report_location = report_path.rstrip(report_path) + reports
    try:
        try:
            if os.path.exists(report_path):
                with open(report_location, 'r+') as f:
                    report_text = f.read()
        except twdataerror.TwDataFileError as twerr:
            twdataerror.TwDataFileError.__str__(twerr)
            raise twdataerror.TwDataFileError(twerr)

        # Checks the text file for report titles that contain church level info
        ch_coords = re.findall(coords, report_text)
        ch_level = re.findall(church_level, report_text)
        ch_list = []
        ch_list_level = []
        for line in ch_coords:
            ch_list.append(line)

        for line in ch_level:
            ch_list_level.append(line)

        ch_comp_list = []

        for i in xrange(0, len(ch_list)):
            ch_comp_list.append((ch_list[i][1], ch_list_level[i]))
        temp_list = []
        for i in xrange(0, len(ch_comp_list)):
            # remove villages without churches from the list
            if ch_comp_list[i][1] == '?':
                temp_list.append(ch_comp_list[i])

        for i in xrange(0, len(temp_list)):
            ch_comp_list.remove(temp_list[i])

        # remove duplicates from the list of church villages
        tst_list = list(set(ch_comp_list))
        ch_comp_list = tst_list
        ch_comp_list.sort()

        # output info 0 prints to a file, this is the default setting
        if output_info == 0:
            output_path = r'' #Your directory path goes here.
            out_file = output_path.rstrip(output_path) + ch_info
            with open(out_file, 'w') as f:
                table_headers = r'[table][**]Village[||]Level[/**]'
                f.write(table_headers)
                for i in xrange(0, len(ch_comp_list)):
                    temp_str = '\n' + "[*][coord]" + ch_comp_list[i][0] + \
                               "[/coord]" + "[|]" + ch_comp_list[i][1]
                    f.write(temp_str)
                f.write("[/table]")
        # returns a list
        elif output_info == 1:
            return ch_comp_list
    except IOError as err:
        print err
