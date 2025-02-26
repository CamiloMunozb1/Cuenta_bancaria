from Funciones_cuenta.nuevo_usuario import IngresoDB, CreacionCuenta


ruta_db = "C:/Users/POWER/cuentas_bancarias.db"
conexion = IngresoDB(ruta_db)

while True:
    print("""
        Bienvenido a tu banco:
        1. Crear cuenta.
        2. Depositar o retirar.
        3. consultar saldo.
        4. mostrar cuentas.
        5. Salir.
    """)
    try:
        usuario = int(input("Ingresa la opcion que desees: "))
        if usuario == 1:
            nueva_cuenta = CreacionCuenta(conexion)
            nueva_cuenta.nueva_cuenta()
        elif usuario == 2:
            print("Funcionalidad proxima.")
        elif usuario == 3:
            print("Funcionalidad proxima.")
        elif usuario == 4:
            print("Funcionalidad proxima.")
        elif usuario == 5:
            print("Gracias por entrar a tu cuenta bancaria.")
            break
        else:
            print("Por favor ingresa una opcion valida del 1 al 5.")
    except Exception as error:
        print(f"Error en el programa: {error}")