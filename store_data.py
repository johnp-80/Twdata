"""
"""
__author__ = 'johnp80'

import csv
import urllib

import MySQLdb
import gntp.notifier
# contains credentials for database.
import database
import getData


class InsertData:
    """class to update database with data from a tribalwars server"""

    def __init__(self):
        self.ally_file = 'ally.txt'
        self.conquer_file = 'conquer.txt'
        self.player_file = 'player.txt'
        self.village_file = 'village.txt'
        self.player_od_file = 'kill_all.txt'
        self.player_oda_file = 'kill_att.txt'
        self.player_odd_file = 'kill_def.txt'
        self.tribe_od_file = 'kill_all_tribe.txt'
        self.tribe_oda_file = 'kill_att_tribe.txt'
        self.tribe_odd_file = 'kill_def_tribe.txt'
        self.update_village = 'updateVillage'
        self.update_ally = 'updateAlly'
        self.update_player = 'updatePlayer'
        self.ally_odt = 'updateAllyODT'
        self.ally_oda = 'updateAllyODA'
        self.ally_odd = 'updateAllyODD'
        self.player_odt = 'updatePlayerODT'
        self.player_oda = 'updatePlayerODA'
        self.player_odd = 'updatePlayerODD'
        self.update_conquer = 'updateConquer'
        self.db = database.Db()
        self.cnx = MySQLdb.Connect(self.db.cnx_params['host'],
                                   self.db.cnx_params['user'],
                                   self.db.cnx_params['pwd'],
                                   self.db.cnx_params['db'])
        self.cursor = self.cnx.cursor()
        self.growl = gntp.notifier.GrowlNotifier(
            applicationName="twData",
            notifications=["database updated"],
            defaultNotifications=["database updated"])
        self.growl.register()

    def db_ally_update(self):
        """
        Updates the ally(tribe) database file
        uses a stored procedure in the database
            to insert or update records
        """
        with open(self.ally_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                row[1] = urllib.unquote_plus(row[1])
                row[2] = urllib.unquote_plus(row[2])
                self.cursor.callproc(self.update_ally, row)
        self.cnx.commit()

    def db_player_update(self):
        """
        Updates the player database file
        uses a stored procedure in the database
            to insert or update records
        """
        with open(self.player_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                row[1] = urllib.unquote_plus(row[1])
                self.cursor.callproc(self.update_player, row)

        self.cnx.commit()

    def db_village_update(self):
        """ Updates the village database file
            uses a stored procedure in the database
            to insert or update records
        """
        with open(self.village_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                row[1] = urllib.unquote_plus(row[1])
                self.cursor.callproc(self.update_village, row)
            self.cnx.commit()

    def db_conquer_update(self):
        """ Updates the conquer database file
            uses a stored procedure to insert new records into the database
        """

        self.cnx.commit()
        with open(self.conquer_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.cursor.callproc(self.update_conquer, row)
        self.cnx.commit()

    def db_od_update(self):
        """
            Updates the opponents defeated tables with new information
        :rtype : None
        """
        # update ally opponents defeated total file
        with open(self.tribe_od_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.cursor.callproc(self.ally_odt, row)
            self.cnx.commit()

        # update ally opponents defeated as attacker
        with open(self.tribe_oda_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.cursor.callproc(self.ally_oda, row)
            self.cnx.commit()

        # update ally opponents defeated as defender
        with open(self.tribe_odd_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.cursor.callproc(self.ally_odt, row)
            self.cnx.commit()

        # update player opponents defeated total
        with open(self.player_od_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.cursor.callproc(self.player_odt, row)
            self.cnx.commit()

        # update player opponents defeated as attacker
        with open(self.player_oda_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.cursor.callproc(self.player_oda, row)
            self.cnx.commit()

        #update player opponents defeated as defender
        with open(self.player_odd_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.cursor.callproc(self.player_odd, row)
            self.cnx.commit()

    def update_all(self):
        """


        """
        self.db_ally_update()
        self.db_conquer_update()
        self.db_od_update()
        self.db_player_update()
        self.db_village_update()
        self.growl.notify(noteType="database updated",
                          title="twData",
                          description="w70 Data updated",
                          sticky=False,
                          priority=1)


def main():
    """


    """
    new_data = getData.TwData('en70')
    update = InsertData()
    new_data.refresh_data()
    update.update_all()

if __name__ == "__main__":
    main()
