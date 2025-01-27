class Config(object): # Configuraciones generales
      DEBUG = True

class ProdConfig(Config): # Configuraciones de producción
    pass

class DevConfig(Config): # Configuraciones de desarollo
    DEBUG = True