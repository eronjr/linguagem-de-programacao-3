import configparser

config = configparser.ConfigParser()

class ConfigMysql:
    __config = config.read('database.ini')
    __secret = config['topsecret.server.com']

    def __init__(self):
        self.username = self.__secret['username']
        self.password = self.__secret['password']
        self.database_name = self.__secret['database_name']
        self.server = self.__secret['server']
        self.port = self.__secret['port']


