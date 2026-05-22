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
        self.cursor = None
        self.conectar()
    def conectar(self):
            try:#
                self.conexion = mariadb.connect(**self.config)
                self.cursor = self.conexion.cursor()
            
            except mariadb.Error as e:
                print(f"ERROR: {e}")
    
    #sirve para insertar modificar o eliminar
    def insertar(self, sql, values):
        self.cursor.execute(sql, values) #aqui va la consulta
        self.conexion.commit()#acepta que se modifiquen los cambios

    #sirve para seleccionar
    def seleccionar(self, sql, values=None):
        self.cursor.execute(sql, values)
        resultado = self.cursor.fetchall()#devuelve todo
        return resultado
    '''def seleccionar(self, sql):
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()#devuelve todo
        return resultado'''
    
 