from conexion import Conexion
from logger_base import log

class CursorDelPool():
    def __init__(self) -> None:
        self._conexion = None
        self._cursor = None
   
    # Este metodo obtiene un cursor llamando al pool de conexiones
    def __enter__(self):
        log.debug(f'Inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug(f'Se ejecuta el metodo __exit__')
        if valor_excepcion:
            self._conexion.roolback()
            log.error(f'Ocurrio una excepcion, se hizo rollback: {valor_excepcion} {tipo_excepcion} {detalle_excepcion}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transaccion') 

        self._cursor.close()
        Conexion.liberarConexion(self._conexion)       

if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('dentro del with')
        cursor.execute('SELECT * FROM usuario')
        log.debug(cursor.fetchall())