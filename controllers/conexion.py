import mysql.connector
from mysql.connector import Error
 
class Conexion:
 
    def __init__(self):
        self.config = {
            "host":     "localhost",
            "user":     "root",
            "password": "",           
            "database": "cloudymusic" 
        }
        self.conexion = None
        self.cursor   = None
 
    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(**self.config)
            self.cursor   = self.conexion.cursor()
            print("Conexión exitosa")
        except Error as e:
            print(f"ERROR: {e}")
 

    def insertar(self, sql, valores):
        self.cursor.execute(sql, valores)
        self.conexion.commit()
 

    def seleccionar(self, sql):
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado
 