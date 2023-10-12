from logger_base import log
from psycopg2 import pool
import sys

class Conexion:
    _DATABASE = 'usuario'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    # Este meteodo realiza la conexion y crea un pool de conexiones
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      database = cls._DATABASE,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      host = cls._HOST,
                                                      port = cls._DB_PORT
                                                      )
                log.debug(f'Creación de pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool')
                sys.exit()
        else:
            return cls._pool 

    # Este metodo llama al Pool y obtiene un anueva conexion
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion Obtenida del Pool: {conexion}')
        return conexion
    
    # Este metodo regresa al Pool de conexiones una conexion
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Devolucion de Conexion al Pool exitosa: {conexion}')

    # Este metodo cierra todas las conexiones
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        log.debug(f'Se cerraron las conexiones existentes')

if __name__== '__main__':
    conexion1 = Conexion().obtenerConexion()
    conexion2 = Conexion().obtenerConexion()
    conexion3 = Conexion().obtenerConexion()
    conexion4 = Conexion().obtenerConexion()
    conexion5 = Conexion().obtenerConexion()
    # retornar conexion al pool
    Conexion.liberarConexion(conexion5)
    # Obtener una nueva conexion es posible porque se libero una
    conexion6 = Conexion().obtenerConexion()
    
