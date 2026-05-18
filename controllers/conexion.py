import mysql.connector
from mysql.connector import Error
import mariadb
 
class Conexion:
    def __init__(self):
        self.config = {
            "host": 'localhost',
            "user": 'root',
            "password": "",           
            "database": "cloudy_music" 
        }
        self.conexion = None
        self.cursor   = None
        self.conectar()
    def conectar(self):
            try:
                self.connection = mariadb.connect(**self.config)
                print("conectado")
                self.cursor = self.connection.cursor()
            
            except Error as e:
                print(f"ERROR: {e}")
    
    #sirve para insertar modificar o eliminar
    def insertar(self, sql, values):
        self.cursor.execute(sql, values) #aqui va la consulta
        self.connection.commit()#acepta que se modifiquen los cambios
    #sirve para seleccionar
    def seleccionar(self, sql):
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()#devuelve todo
        return resultado
    
 