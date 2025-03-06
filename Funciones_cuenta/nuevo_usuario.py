import sqlite3  # IMPORTAMOS LA BIBLIOTECA PARA MANEJAR BASES DE DATOS SQLITE

# CLASE PARA MANEJAR LA CONEXIÓN A LA BASE DE DATOS
class IngresoDB:
    def __init__(self, conexion):
        try:
            self.conn = sqlite3.connect(conexion)  # ESTABLECEMOS LA CONEXIÓN CON LA BASE DE DATOS
            self.cursor = self.conn.cursor()  # CREAMOS UN CURSOR PARA EJECUTAR CONSULTAS SQL
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")  # MANEJO DE ERRORES EN LA CONEXIÓN

    def cerrar_conexion(self):
        """MÉTODO PARA CERRAR LA CONEXIÓN CON LA BASE DE DATOS."""
        self.conn.close()
        print("Conexión con base de datos cerrada.")  # MENSAJE DE CONFIRMACIÓN


# CLASE PARA LA CREACIÓN DE CUENTAS EN LA BASE DE DATOS
class CreacionCuenta:
    def __init__(self, conexion):
        self.conexion = conexion  # SE RECIBE LA CONEXIÓN A LA BASE DE DATOS

    def nueva_cuenta(self):
        try:
            cuenta_nombre = input("Ingresa el nombre para la cuenta: ").strip()  # ELIMINAMOS ESPACIOS EN BLANCO INNECESARIOS
            cuenta_apellido = input("Ingresa el apellido de la cuenta: ").strip()

            # VALIDAMOS QUE NO ESTÉN VACÍOS
            if not cuenta_nombre or not cuenta_apellido:
                print("El nombre y apellido no pueden estar vacíos.")
                return

            # INSERTAMOS LOS DATOS EN LA BASE DE DATOS
            self.conexion.cursor.execute(
                "INSERT INTO cuenta_banco (nombre_cuenta, apellido_cuenta) VALUES (?, ?)",
                (cuenta_nombre, cuenta_apellido)
            )
            self.conexion.conn.commit()  # GUARDAMOS LOS CAMBIOS EN LA BASE DE DATOS

            print(f"Cuenta a nombre: {cuenta_nombre} {cuenta_apellido}, creada exitosamente.")

        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")  # CAPTURA DE ERRORES DE SQLITE
        except Exception as error:
            print(f"Error en el programa: {error}")  # CAPTURA DE ERRORES GENERALES


# DEFINIMOS LA RUTA DE LA BASE DE DATOS
ruta_db = "C:/Users/POWER/cuentas_bancarias.db"

# CREAMOS UNA INSTANCIA DE CONEXIÓN A LA BASE DE DATOS
conexion = IngresoDB(ruta_db)

