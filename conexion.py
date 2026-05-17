import mysql.connector
from mysql.connector import Error
import mariadb

class Conexion:
    def __init__(self):
        self.config = {
        "host":'localhost',
        "user":"root",
        "password":"",
        "db":"prueba_python"
        }
        self.conexion = None
        self.cursor = None
    def conectar(self):
        try:
            self.conexion = mariadb.connect(**self.config)
            print("Conexión exitosa")
            self.cursor = self.conexion.cursor()
        except Error as e:
            print(f"ERROR: {e}")
    #Sirve para insertar modificar o eliminar
    def insertar(self, sql, valores):
        self.cursor.execute(sql,valores)
        self.conexion.commit()
    #Sirve para seleccionar bonito
    def seleccionar(self, sql):
        self.cursor.execute(sql)
        resultado = self.cursor.fetchal00l()
        return resultado