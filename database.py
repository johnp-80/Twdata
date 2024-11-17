"""database.py
Handles the database connection, and all stored procedures.
    :rtype: None"""

import os.path

import ConfigParser
import MySQLdb

__author__ = 'johnp80'
__email__ = 'johnp90380@gmail.com'


class Db:
    """Base class for establishing a database connection.
    :param host: ip address or domain name of server where database is located
    :param user: user name of database user
    :param pwd: password
    :param db: name of database.
    :param config_file: config file containing database cnx information and the
    tribalwars server information
    """

    def __init__(self, host='', user='', pwd='', db='', config_file='config.ini'):
        """

        :param config_file: configuration file.
        :type var config_file: str
        :type var host: str
        :type var user: str
        :type var pwd: str
        :type var db: str
        :param host: the host ip address or domain, where the database
        is located
        :param user: mysql user name should be specific to the application.
        :param pwd: password for the database. On production, this should be
        a prompt for the password, or stored in a protected config file.
        :param db: the server name, which corresponds with the database
        the user is trying to access
        """
        self.parser = ConfigParser.SafeConfigParser()
        self.config_file = config_file
        self.__host = host
        self.__user = user
        self.__pwd = pwd
        self.__db = db
        if os.path.isfile(config_file):
            self.parser.read(self.config_file)
            self.__user = self.parser.get('mysql', 'user')
            self.__pwd = self.parser.get('mysql', 'pw')
            self.__db = self.parser.get('mysql', 'db')
        else:
            self.get_config(self.config_file, host, user, pwd, db)


        self.cnx_params = dict(host=self.__host, user=self.__user,
                               pwd=self.__pwd, db=self.__db)

    def get_config(self, config_file, host, user, pwd, db):
        if os.path.isfile(config_file):
            pass
        else:
            try:
                self.parser.add_section('mysql')
                self.parser.add_section('mysql')
                self.parser.set('mysql', 'host', host)
                self.parser.set('mysql', 'user', user)
                self.parser.set('mysql', 'pw', pwd)
                self.parser.set('mysql', 'db', db)
                with open(self.config_file, 'w') as cfg:
                    self.parser.write(cfg)
            except ConfigParser.NoSectionError, err:
                print '{}:{}'.format('error:', err)
            except ConfigParser.DuplicateSectionError, err:
                print str(err)
            except ConfigParser.MissingSectionHeaderError, err:
                print str(err)
            except ConfigParser.ParsingError, err:
                print str(err)
            except ConfigParser.NoOptionError, err:
                print str(err)
            except ConfigParser.Error, err:
                print str(err)

    def sp_db_query(self, query, *args):
        """Executes a stored procedure
            :param query: executes a stored procedure on the mysql database
            :param args:the applicable arguments for the db query
            :return: results of the executed query.
            """
        try:
            d = MySQLdb.Connect(self.cnx_params["host"],
                                self.cnx_params["user"],
                                self.cnx_params["pwd"],
                                self.cnx_params['db'])
            cursor = d.cursor()
            cursor.callproc(query, args)
            result = cursor.fetchall()
            return result
        except MySQLdb.Warning, warn:
            print(warn)
        except MySQLdb.OperationalError, err:
            print(err)
        except MySQLdb.ProgrammingError, err:
            print str(err)
        except MySQLdb.NotSupportedError, err:
            print str(err)
        except MySQLdb.InterfaceError, err:
            print str(err)
        except MySQLdb.MySQLError, err:
            print str(err)
        except MySQLdb.DatabaseError, err:
            print str(err)
        except MySQLdb.DataError, err:
            print str(err)
        except MySQLdb.Error, err:
            print str(err)

def main():
    """

    :rtype : object
    """
    d = Db()
    cnx = MySQLdb.Connect(d.cnx_params['host'], d.cnx_params['user'],
                          d.cnx_params['pwd'], 'w70')
    cursor = cnx.cursor()



if __name__ == '__main__':
    main()