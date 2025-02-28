# Cuenta Bancaria

Este proyecto es un sistema de gestión de cuentas bancarias utilizando **Python** y **SQLite**. Permite la creación de cuentas, consulta de cuentas existentes, visualización de saldos, ingreso y retiro de dinero.

## Características
- Creación de nuevas cuentas bancarias.
- Consulta de cuentas registradas en la base de datos.
- Visualización de saldos de cuentas.
- Ingreso de dinero a una cuenta específica.
- Retiro de dinero de una cuenta específica.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.x
- SQLite3 (incluido en Python por defecto)
- Pandas (para consultas y manejo de datos en la base de datos)

Para instalar Pandas, usa el siguiente comando:
```sh
pip install pandas
```

## Estructura del Proyecto

- `ingreso_db.py`: Módulo encargado de manejar la conexión a la base de datos.
- `creacion_cuenta.py`: Módulo para la creación de cuentas.
- `mostrar_cuentas.py`: Permite consultar las cuentas registradas.
- `mostrar_saldos.py`: Permite visualizar los saldos de las cuentas.
- `ingreso_dinero.py`: Funcionalidad para depositar dinero en una cuenta.
- `retiro_dinero.py`: Funcionalidad para retirar dinero de una cuenta.

## Uso

### 1. Crear una cuenta nueva
Ejecuta el archivo `creacion_cuenta.py` e ingresa el nombre y apellido de la cuenta:
```sh
python creacion_cuenta.py
```

### 2. Consultar cuentas registradas
Ejecuta el archivo `mostrar_cuentas.py`:
```sh
python mostrar_cuentas.py
```

### 3. Consultar saldos de las cuentas
Ejecuta el archivo `mostrar_saldos.py`:
```sh
python mostrar_saldos.py
```

### 4. Ingresar dinero a una cuenta
Ejecuta `ingreso_dinero.py` e ingresa los datos solicitados:
```sh
python ingreso_dinero.py
```

### 5. Retirar dinero de una cuenta
Ejecuta `retiro_dinero.py` e ingresa los datos solicitados:
```sh
python retiro_dinero.py
```

## Base de Datos

El proyecto utiliza una base de datos SQLite con las siguientes tablas:

- **cuenta_banco**: Contiene la información de las cuentas (ID, nombre y apellido).
- **saldo_cuentas**: Almacena el saldo actual de cada cuenta.

## Contribución
Si deseas mejorar el proyecto, puedes hacer un fork del repositorio y enviar tus propuestas a través de pull requests.

## Autor
Proyecto desarrollado por **CamiloMuñozb1**

## Licencia
Este proyecto se distribuye bajo la licencia **MIT**.

