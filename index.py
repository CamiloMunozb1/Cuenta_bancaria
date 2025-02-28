# Importamos las clases necesarias desde los módulos correspondientes
from Funciones_cuenta.nuevo_usuario import IngresoDB, CreacionCuenta
from Funciones_cuenta.depositar_retirar import IngresoDB, DepositarRetirar
from Funciones_cuenta.consultar_saldo import IngresoDB, MostrarSaldos
from Funciones_cuenta.consulta_cuentas import IngresoDB, MostrarCuentas

# Definimos la ruta de la base de datos
ruta_db = "C:/Users/POWER/cuentas_bancarias.db"

# Creamos una conexión a la base de datos utilizando la clase IngresoDB
conexion = IngresoDB(ruta_db)

# Bucle infinito para mostrar el menú hasta que el usuario decida salir
while True:
    # Mostramos el menú de opciones para el usuario
    print("""
        Bienvenido a tu banco:
        1. Crear cuenta.
        2. Depositar o retirar.
        3. Consultar saldo.
        4. Mostrar cuentas.
        5. Salir.
    """)

    try:
        # Solicitamos al usuario que ingrese una opción
        usuario = int(input("Ingresa la opción que desees: "))

        # Opción 1: Crear una nueva cuenta bancaria
        if usuario == 1:
            nueva_cuenta = CreacionCuenta(conexion)  # Instancia de la clase CreacionCuenta
            nueva_cuenta.nueva_cuenta()  # Llamamos al método para crear una nueva cuenta

        # Opción 2: Depositar o retirar dinero
        elif usuario == 2:
            depositar_retirar = DepositarRetirar(conexion)  # Instancia de la clase DepositarRetirar
            depositar_retirar.ejecutar_opciones()  # Llamamos al método para realizar la operación

        # Opción 3: Consultar el saldo de una cuenta
        elif usuario == 3:
            consulta_saldo = MostrarSaldos(conexion)  # Instancia de la clase MostrarSaldos
            consulta_saldo.consulta_saldo()  # Llamamos al método para consultar el saldo

        # Opción 4: Mostrar todas las cuentas registradas
        elif usuario == 4:
            consulta_cuentas = MostrarCuentas(conexion)  # Instancia de la clase MostrarCuentas
            consulta_cuentas.consulta_cuentas()  # Llamamos al método para mostrar las cuentas

        # Opción 5: Salir del programa
        elif usuario == 5:
            print("Gracias por entrar a tu cuenta bancaria.")
            break  # Terminamos el bucle y finalizamos el programa

        # Validación en caso de ingresar una opción incorrecta
        else:
            print("Por favor ingresa una opción válida del 1 al 5.")

    # Manejo de errores en caso de que el usuario ingrese un valor no numérico
    except ValueError:
        print("Error de validación de entrada, ingresa un valor numérico correcto.")

    # Captura cualquier otro error inesperado
    except Exception as error:
        print(f"Error en el programa: {error}")
