# <h1 align=center> **Usuarios_DB** </h1>

<p align="center">
<img src="./recursos/logo.png"  height=300>
</p>


# Autor Diego Maneyro

+ [linkedin](https://www.linkedin.com/in/diego-maneyro/)

+ [E-mail](diegomaneyro@gmail.com)

# Base de Datos de Usuarios en PostgreSQL con Python

Este proyecto consiste en la creación de una base de datos de usuarios utilizando Python y PostgreSQL, para administrar datos de usuarios.

# Estructura de Proyecto

<p align="center">
<img src="./recursos/estructuraProyecto.png"  height=300>
</p>

## Deployment

Clonar este proyecto

```bash
  git clone https://github.com/diegomaneyro/Usuarios_DB.git
```

Instalar librerias

```bash
  pip install -r > requirements.txt
```

Ejecutar App

```bash
  python.exe menu_app_usuario.py 
```


## Uso de la App
* Menu Principal:
<p align="center">
<img src="./recursos/MenuPrincipal.png"  height=150>
</p>


## App Usuarios:
### Listar usuarios  

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Opcion 1` | `SELECT` | **Parametro**. None |



### Agregar usuario  

| Parameter | Type     | Description                          |
| :-------- | :------- | :----------------------------------- |
| `Opcion 2` | `INSERT` | **Parametro**. (Username, password) |


### Modificar usuario  

| Parameter | Type     | Description                  |
| :-------- | :------- | :--------------------------- |
| `Opcion 3` | `UPDATE` | **Parametro**. (id_usuario,
Username, password) |

### Eliminar usuario  

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Opcion 4` | `DELETE` | **Parametro**. (id_usuario) |

### Salir

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Opcion 5` | `Exit` | **Parametro**. None |


## License

[MIT](https://choosealicense.com/licenses/mit/)