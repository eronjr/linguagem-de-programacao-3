import os
import random, string
from read_config import ConfigMysql

sql = ConfigMysql()


class Config(object):
    CSRF_ENABLED = True #habilita criptografia
    SECRET = 'ysb_92=qe#djf8%ng+a*#4rt#5%3*4k5%i2bck*gn@w3@f&-&' #criar chaves...
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     'templates') #caminho para o local
                                                  #onde os arquivos de template ficarão
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) #caminho do local onde a raiz                                                            #do projeto se contra
    APP = None #propriedade do app
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{server}/{database_name}".format(
        username=sql.username,
        password=sql.password,
        server=sql.server,
        database_name=sql.database_name
    )

    #Preencha com os dados do seu banco de dados
    # User - Usuário do banco
    # Passwd - Senha do usuário
    # Host - Geralmente no local fica localhost
    # Port - Geralmente 3306 no mysql
    # Database - Nome do banco de dados

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    IP_HOST = 'localhost' # Aqui geralmente é um IP de um servidor na
    #nuvem e não o endereço da máquina local
    PORT_HOST = 5000
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    IP_HOST = 'localhost' # Aqui geralmente é um IP de um servidor na
    #nuvem e não o endereço da máquina local
    PORT_HOST = 8080
    URL_MAIN = 'http://%s:%s/' % (IP_HOST, PORT_HOST)

app_config = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()
}

app_active = os.getenv('FLASK_ENV')
