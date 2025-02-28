import sqlite3
import pandas as pd

# CLASE PARA MANEJAR LA CONEXIÓN A LA BASE DE DATOS
class IngresoDB:
    def __init__(self, conexion):
        try:
            # ESTABLECE LA CONEXIÓN A LA BASE DE DATOS
            self.conn = sqlite3.connect(conexion)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            # MANEJO DE ERRORES EN CASO DE FALLA AL CONECTARSE
            print(f"Error en la base de datos: {error}.")

    def cerrar_conexion(self):
        # CIERRA LA CONEXIÓN A LA BASE DE DATOS
        self.conn.close()
        print("Conexion con base de datos cerrada.")

# CLASE PARA CONSULTAR LAS CUENTAS REGISTRADAS EN LA BASE DE DATOS
class MostrarCuentas:
    def __init__(self, conexion):
        self.conexion = conexion
    
    def consulta_cuentas(self):
        try:
            # CONSULTA SQL PARA OBTENER LOS NOMBRES Y APELLIDOS DE LAS CUENTAS REGISTRADAS
            query = """
                    SELECT 
                        cuenta_banco.nombre_cuenta,
                        cuenta_banco.apellido_cuenta
                    FROM cuenta_banco
                """
            # EJECUTA LA CONSULTA Y OBTIENE LOS RESULTADOS EN UN DATAFRAME DE PANDAS
            resultado = pd.read_sql_query(query, self.conexion.conn)
            
            # SI HAY RESULTADOS, SE MUESTRAN; SI NO, SE NOTIFICA QUE NO HAY CUENTAS
            if not resultado.empty:
                print(resultado)
            else:
                print("No se encontraron saldos.")
        except sqlite3.Error as error:
            # MANEJO DE ERRORES DE BASE DE DATOS
            print(f"Error en la base de datos: {error}.")
        except Exception as error:
            # MANEJO DE ERRORES GENERALES
            print(f"Error en el programa: {error}.")

# RUTA A LA BASE DE DATOS
ruta_db = "C:/Users/POWER/cuentas_bancarias.db"
# SE CREA UNA INSTANCIA DE LA CLASE PARA LA CONEXIÓN A LA BASE DE DATOS
conexion = IngresoDB(ruta_db)
