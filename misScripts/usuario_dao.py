from usuario import Usuario
from logger_base import log
from cursor_del_pool import CursorDelPool

class UsuarioDAO:
    '''
    DAO - Data Access Object para la tala de usuario
    CRUD - Create - Read - Update - Delete para la tabla de usuario
    '''
       
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando Usuario')
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios 
        
    @classmethod    
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)            
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a actualizar: {usuario}')
            valores = (usuario.username, usuario.password, usuario.id_usuario )
            cursor.execute(cls._ACTUALIZAR, valores)            
            return cursor.rowcount
           
    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a eliminar: {usuario}')
            valores = (usuario.id_usuario, )
            cursor.execute(cls._ELIMINAR, valores)            
            return cursor.rowcount
        
if __name__ == '__main__':
    
    '''   
    # Actualizar usuarios
    usuario1 = Usuario(username='MauroDaniel', password='mauro1524545', id_usuario=19)
    usuario_actualizado = UsuarioDAO.actualizar(usuario1)
    log.info(f'Usuario actualizado: {usuario_actualizado}')
    '''   
    # Eliminar usuarios
    usuario = Usuario(id_usuario=19)
    usuario_eliminado = UsuarioDAO.eliminar(usuario)
    log.info(f'Usuario eliminado: {usuario_eliminado}')
        
    # Seleccionar usuario
    usuarios = UsuarioDAO().seleccionar()
    for usuario in usuarios:
        log.info(usuario)
     