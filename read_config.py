import configparser
import os

config = configparser.ConfigParser()

class ConfigMysql:
    # __config = config.read('database.ini')
    # __secret = config['topsecret.server.com']

    def __init__(self):
        # self.username = self.__secret['username']
        # self.password = self.__secret['password']
        # self.database_name = self.__secret['database_name']
        # self.server = self.__secret['server']
        # self.port = self.__secret['port']

        self.username = os.environ['mysql_username']
        self.password = os.environ['mysql_password']
        self.database_name = os.environ['mysql_database_name']
        self.server = os.environ['mysql_server']
        self.port = os.environ['mysql_port']