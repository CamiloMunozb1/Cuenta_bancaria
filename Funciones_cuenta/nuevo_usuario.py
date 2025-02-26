import sqlite3

class IngresoDB:
    def __init__(self, conexion):
        try:
            self.conn = sqlite3.connect(conexion)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")

    def cerrar_conexion(self):
        self.conn.close()
        print("Conexion con base de datos cerrada.")


class CreacionCuenta:
    def __init__(self, conexion):
        self.conexion = conexion

    def nueva_cuenta(self):
        try:
            cuenta_nombre = str(input("Ingresa el nombre para la cuenta: "))
            cuenta_apellido = str(input("Ingresa el apellido de la cuenta: "))
            self.conexion.cursor.execute("INSERT INTO cuenta_banco (nombre_cuenta,apellido_cuenta) VALUES (?,?)",(cuenta_nombre,cuenta_apellido))
            self.conexion.conn.commit()
            print(f"Cuenta a nombre: {cuenta_nombre} y apellido: {cuenta_apellido}, creada exitosamente.")
        except ValueError:
            print("Ingresa un valor correxto.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")
        except Exception as error:
            print(f"Error en el programa: {error}")


ruta_db = "C:/Users/POWER/cuentas_bancarias.db"
conexion = IngresoDB(ruta_db)