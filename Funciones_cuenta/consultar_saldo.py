import sqlite3
import pandas as pd

# CLASE PARA MANEJAR LA CONEXIÓN A LA BASE DE DATOS
class IngresoDB:
    def __init__(self, conexion):
        try:
            # ESTABLECER CONEXIÓN CON LA BASE DE DATOS
            self.conn = sqlite3.connect(conexion)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")

    def cerrar_conexion(self):
        # CERRAR LA CONEXIÓN CON LA BASE DE DATOS
        self.conn.close()
        print("Conexion con base de datos cerrada.")

# CLASE PARA MOSTRAR SALDOS DE LAS CUENTAS
class MostrarSaldos:
    def __init__(self, conexion):
        self.conexion = conexion
    
    def consulta_saldo(self):
        try:
            # CONSULTA PARA OBTENER LOS SALDOS DE LAS CUENTAS
            query = """
                    SELECT 
                        cuenta_banco.nombre_cuenta,
                        cuenta_banco.apellido_cuenta,
                        saldo_cuentas.saldo_cuenta
                    FROM cuenta_banco
                    JOIN saldo_cuentas ON cuenta_banco.cuenta_id = saldo_cuentas.cuenta_id
                """
            # EJECUTAR LA CONSULTA Y OBTENER LOS RESULTADOS EN UN DATAFRAME
            resultado = pd.read_sql_query(query, self.conexion.conn)
            
            # VERIFICAR SI HAY RESULTADOS Y MOSTRARLOS
            if not resultado.empty:
                print(resultado)
            else:
                print("No se encontraron saldos.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")
        except Exception as error:
            print(f"Error en el programa: {error}.")

# DEFINIR LA RUTA DE LA BASE DE DATOS Y CREAR LA CONEXIÓN
ruta_db = "C:/Users/POWER/cuentas_bancarias.db"
conexion = IngresoDB(ruta_db)
