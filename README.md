# Repositorio proyecto de prueba Python FastApi SQLAlchemy MySQL


### Librerías :
- FastApi: [Documentación de FastApi](https://fastapi.tiangolo.com/)
- SQLAlchemy: [Documentación de SQLAlchemy](https://docs.sqlalchemy.org/en/20/)


## Estructura 
## Raiz
```
.
Python-FastApi-MySQL-SQLAlchemy /
|-- app/
|   |-- main.py
|   |-- api/
|   |   |-- endpoints/
|   |   |   |-- usersEndPoints.py
|   |   |   |-- auth.py
|   |   |-- models/
|   |   |   |-- modelsUsers.py
|   |-- core/
|   |   |-- auth.py
|-- service/
|   |-- databaseConfig.py
|-- utils/
|   |-- servicesTable.py
|   |-- subscriptionTable.py
|   |-- usersTable.py
|-- main.py
|-- .env.example
|-- .gitignore
|-- requirements.txt
|-- README.md

```


## Instalación

Sigue estos pasos para configurar el proyecto localmente:

1. Clona el repositorio:

```bash
git clone https://github.com/sebastianmiracastro/Python_FastApi_SQLAlchemy_MySQL.git
```
Crea y activa un entorno virtual:


```
python3 -m venv nombre_del_entorno_virtual
source nombre_del_entorno_virtual/bin/activate
```
Instala las dependencias del proyecto:
```
pip install -r requirements.txt
```

## Paso a Paso

Abre una terminal y navega a la carpeta raíz de tu proyecto.
Crea un nuevo entorno virtual con venv usando el siguiente comando:


```
python3 -m venv venv
```
Activa el entorno Virtual.
```
./venv/Scripts/Activate
```
Instalar con pip:
```
$ pip install -r requirements.txt
```
```
$ uvicorn main:app --reload
```
## Requisito 

Este proyecto tiene los siguientes endpoints:




| Name                             | Stmts | Miss | Cover |
|----------------------------------|-------|------|-------|
| SuscripcionesApp\admin.py         | 1     | 0    | 100%  |
| SuscripcionesApp\apps.py          | 4     | 0    | 100%  |
| SuscripcionesApp\models.py        | 16    | 2    | 88%   |
| SuscripcionesApp\serializers.py   | 10    | 0    | 100%  |
| SuscripcionesApp\tests.py         | 63    | 0    | 100%  |
| SuscripcionesApp\views.py         | 80    | 40   | 50%   |
| UsuariosApp\admin.py              | 1     | 0    | 100%  |
| UsuariosApp\apps.py               | 4     | 0    | 100%  |
| UsuariosApp\models.py             | 10    | 1    | 90%   |
| UsuariosApp\serializers.py        | 6     | 0    | 100%  |
| UsuariosApp\tests.py              | 41    | 0    | 100%  |
| UsuariosApp\views.py              | 34    | 12   | 65%   |
|----------------------------------|-------|------|-------|
| TOTAL                            | 270   | 55   | 80%   |

## Swagger

Adicional tiene una documentacion corta en postman

https://documenter.getpostman.com/view/17377152/2s93m354EM#aa600443-bcce-454e-bac4-9befed7e1486

