"""
Tool to quickly import tribal wars data from their servers.
uses: os, os.path, gzip, time, and requests

"""

import os
import os.path
import gzip
import time

import requests


__author__ = "johnp80"
__contact__ = "johnp90380@gmail.com"


class TwData:
    """

    :param server:
    """

    def __init__(self, server):
        """

        :param server: the tribal wars server to download data from
        """
        self.server = server
        self.data_files = ["village.txt.gz", "player.txt.gz", "ally.txt.gz",
                           "kill_att.txt.gz", "kill_def.txt.gz",
                           "kill_all.txt.gz", "kill_att_tribe.txt.gz",
                           "kill_def_tribe.txt.gz",
                           "kill_all_tribe.txt.gz"]
        self.data_files_new = ["village.txt", "player.txt", "ally.txt",
                               "kill_att.txt", "kill_def.txt",
                               "kill_all.txt", "kill_att_tribe.txt",
                               "kill_def_tribe.txt",
                               "kill_all_tribe.txt"]
        self.url_protocol = "http://"
        self.url_data = ".tribalwars.net/map/"
        self.tw_req = requests.Request.url = \
            self.url_protocol + self.server + self.url_data
        self.tw_conq_url = '/interface.php?func=get_conquer&since='
        self.tw_conq = requests.Request.url = \
            self.url_protocol + self.server + '.tribalwars.net/' + \
            self.tw_conq_url
        self.conquer_file = "conquer.txt"
        self.all_conquers = ["conquer.txt.gz"]
        self.conquer_log = "last_update.txt"
        self.last_update = 0

    @staticmethod
    def fetch_files(data_files, tw_req):
        """

        :type data_files: list
        :param data_files: original files to download from server
        :param tw_req: location to download files from
        """
        for data_file in xrange(0, len(data_files)):
            f = requests.get(tw_req + data_files[data_file])
            with open(data_files[data_file], "wb") as d:
                d.write(f.content)

    @staticmethod
    def get_data(data_files, data_files_new):
        """

        :param data_files: compressed files downloaded from server
        :param data_files_new: uncompressed files.
        """
        for i in xrange(0, len(data_files)):
            with gzip.open(data_files[i], 'rb') as f:
                data = f.read()
                with open(data_files_new[i], "wb") as x:
                    x.write(data)

    @staticmethod
    def clean_files(data_files):
        """

        :param data_files: compressed files to remove
        """
        for x in xrange(0, len(data_files)):
            try:
                os.remove(data_files[x])
            except OSError:
                pass

    def update_conquers(self):
        """Downloads the most recent conquers. If the data is more than
            24 hours old, the entire table will be replaced with new data.
        """
        if os.path.isfile(self.conquer_log):
            with open(self.conquer_log, 'r') as c:
                self.last_update = c.read()
            if self.last_update > (int(time.time() - 3600)):
                self.fetch_files(self.all_conquers, self.tw_req)
                self.get_data(self.all_conquers, list(self.conquer_file))
                self.clean_files(self.all_conquers)
            else:
                f = requests.get(self.tw_conq + self.last_update)
                with open(self.conquer_file, 'w') as c:
                    c.write(f.content)
        else:
            self.fetch_files(self.all_conquers, self.tw_req)
            self.get_data(self.all_conquers, list(self.conquer_file))
            self.clean_files(self.all_conquers)
        t = time.time()
        with open(self.conquer_log, 'w') as c:
            t_stamp = int(t)
            c.write(str(t_stamp))

    def refresh_data(self):
        """Wraps the entire data gathering operation into a single function call
        """
        self.fetch_files(self.data_files, self.tw_req)
        self.get_data(self.data_files, self.data_files_new)
        self.update_conquers()
        self.clean_files(self.data_files)


def main():
    """
    downloads information about the specified tribalwars server.

    refresh_data() will attempt to download all the files and unzip them.
    fetch_files() will download the zipped files
    get_data() will unzip the files
    clean_files() will remove the (zipped) files by default. Given a different
    argument, it will remove other files in the directory

    """
    data = TwData('en70')
    data.refresh_data()


if __name__ == '__main__':
    main()