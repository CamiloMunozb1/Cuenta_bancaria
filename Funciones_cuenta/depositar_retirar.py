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

class DepositarRetirar:
    def __init__(self,conexion):
        self.conexion = conexion
        self.opciones = {
            "1": self.opcion_uno,
            "2": self.opcion_dos
        }
    
    def mostrar_opciones(self):
        print("""
                Que operacion deseas realizar?
                1. Depositar.
                2. Retirar.
            """)
    
    def ejecutar_opciones(self):
        while True:
            self.mostrar_opciones()
            usuario = str(input("Ingresa una opcion: "))
            accion = self.opciones.get(usuario)
            if accion:
                accion()
                break
    
    def saldos_nuevos(self):
        try:
            nombre_cuenta = str(input("Ingresa el nombre del titular de la cuenta: "))
            apellido_cuenta = str(input("Ingresa el apellido del titular de la cuenta: "))
            ingreso_saldos = float(input("Ingresa el saldo a tu cuenta: "))
            self.conexion.cursor.execute("SELECT cuenta_ID FROM cuenta_banco WHERE nombre_cuenta = ? AND apellido_cuenta = ?",(nombre_cuenta,apellido_cuenta))
            cuenta = self.conexion.cursor.fetchone()
            if cuenta:
                cuenta_id = cuenta[0]
                if ingreso_saldos > 0:
                    self.conexion.cursor.execute("INSERT INTO saldo_cuentas (saldo_cuenta, cuenta_id) VALUES (?,?)",(ingreso_saldos,cuenta_id))
                    self.conexion.conn.commit()
                    print(f"Saldo de: {ingreso_saldos} ingresado correctamente en la cuenta.")
                else:
                    print(f"El valor de {ingreso_saldos} no puede ser 0.")
            else:
                print("El titular no existe volver a intentar o crear una cuenta nueva.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")
        except Exception as error:
            print(f"Error en el programa: {error}")
    
    def retiro_dinero(self):
        try:
            nombre_cuenta = str(input("Ingresa el nombre del titular de la cuenta: "))
            apellido_cuenta = str(input("Ingresa el apellido del titular de la cuenta: "))
            retiro_saldo = float(input("Ingresa la cantidad a retirar: ")) 
            self.conexion.cursor.execute("SELECT cuenta_ID FROM cuenta_banco WHERE nombre_cuenta = ? AND apellido_cuenta = ?",(nombre_cuenta,apellido_cuenta))
            cuenta = self.conexion.cursor.fetchone()
            if cuenta:
                cuenta_id = cuenta[0]
                self.conexion.cursor.execute("SELECT saldo_cuenta FROM saldo_cuentas WHERE cuenta_id = ?",(cuenta_id,))
                saldo = self.conexion.cursor.fetchone()
                if saldo:
                    saldo_cuenta = saldo[0]
                    if 0 < retiro_saldo <= saldo_cuenta:
                        nuevo_saldo = saldo_cuenta - retiro_saldo
                        self.conexion.cursor.execute("UPDATE saldo_cuentas SET saldo_cuenta = ? WHERE cuenta_id = ?",(nuevo_saldo,cuenta_id))
                        self.conexion.conn.commit()
                        print(f"Retiro exitoso. Nuevo saldo: {nuevo_saldo}")
                    else:
                        print("Saldo insuficiente o monto invalido.")
                else:
                    print("No se encontro el saldo para la cuenta.")
            else:
                print("Cuenta no encontrada")
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")
        except Exception as error:
            print(f"Error en el programa: {error}.")

    def opcion_uno(self):
        self.saldos_nuevos()
    def opcion_dos(self):
        self.retiro_dinero()


ruta_db = "C:/Users/POWER/cuentas_bancarias.db"
conexion = IngresoDB(ruta_db)

if __name__ == "__main__":
    opciones = DepositarRetirar(conexion)
    opciones.ejecutar_opciones()