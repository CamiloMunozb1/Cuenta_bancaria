import sqlite3

# CLASE PARA MANEJAR LA CONEXIÓN A LA BASE DE DATOS
class IngresoDB:
    def __init__(self, conexion):
        try:
            self.conn = sqlite3.connect(conexion)  # ESTABLECER CONEXIÓN CON LA BASE DE DATOS
            self.cursor = self.conn.cursor()  # CREAR UN CURSOR PARA EJECUTAR CONSULTAS SQL
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}.")

    def cerrar_conexion(self):
        self.conn.close()  # CERRAR LA CONEXIÓN CUANDO YA NO SE NECESITE
        print("Conexion con base de datos cerrada.")

# CLASE PARA DEPOSITAR Y RETIRAR DINERO
class DepositarRetirar:
    def __init__(self,conexion):
        self.conexion = conexion  # SE RECIBE LA CONEXIÓN A LA BASE DE DATOS
        self.opciones = {
            "1": self.opcion_uno,  # OPCIÓN PARA DEPOSITAR DINERO
            "2": self.opcion_dos   # OPCIÓN PARA RETIRAR DINERO
        }
    
    # MÉTODO PARA MOSTRAR LAS OPCIONES DISPONIBLES
    def mostrar_opciones(self):
        print("""
                Que operacion deseas realizar?
                1. Depositar.
                2. Retirar.
            """)
    
    # MÉTODO PARA EJECUTAR LA OPERACIÓN SELECCIONADA
    def ejecutar_opciones(self):
        while True:
            try:
                self.mostrar_opciones()
                usuario = str(input("Ingresa una opcion: "))
                accion = self.opciones.get(usuario)  # SE OBTIENE LA FUNCIÓN ASOCIADA A LA OPCIÓN
                if accion:
                    accion()  # SE EJECUTA LA FUNCIÓN CORRESPONDIENTE
                    break
                else:
                    print("Ingresa un valor correcto entre 1 y 2")
            except ValueError:
                print("Ingresa un valor valido")
    
    # MÉTODO PARA DEPOSITAR DINERO EN UNA CUENTA
    def saldos_nuevos(self):
        try:
            nombre_cuenta = str(input("Ingresa el nombre del titular de la cuenta: ")).strip()
            apellido_cuenta = str(input("Ingresa el apellido del titular de la cuenta: ")).strip()
            ingreso_saldos = float(input("Ingresa el saldo a tu cuenta: "))
            if not nombre_cuenta or not apellido_cuenta:
                print("El nombre y el apellido no pueden estar vacios.")
                return
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
    
    # MÉTODO PARA RETIRAR DINERO DE UNA CUENTA
    def retiro_dinero(self):
        try:
            nombre_cuenta = str(input("Ingresa el nombre del titular de la cuenta: ")).strip()
            apellido_cuenta = str(input("Ingresa el apellido del titular de la cuenta: ")).strip()
            retiro_saldo = float(input("Ingresa la cantidad a retirar: "))
            if not nombre_cuenta or not apellido_cuenta:
                print("El nombre y el apellido no pueden estar vacios.")
                return
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

    # MÉTODO PARA EJECUTAR LA OPCIÓN DE DEPOSITAR
    def opcion_uno(self):
        self.saldos_nuevos()
    
    # MÉTODO PARA EJECUTAR LA OPCIÓN DE RETIRAR
    def opcion_dos(self):
        self.retiro_dinero()

# DEFINIR LA RUTA DE LA BASE DE DATOS
ruta_db = "C:/Users/POWER/cuentas_bancarias.db"
conexion = IngresoDB(ruta_db)

# EJECUTAR EL PROGRAMA SI SE LLAMA DIRECTAMENTE
if __name__ == "__main__":
    opciones = DepositarRetirar(conexion)
    opciones.ejecutar_opciones()
