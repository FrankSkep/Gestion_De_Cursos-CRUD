import mysql.connector
from mysql.connector import Error

class ConexionBD():
   def __init__(self):
      try:
         self.conexion = mysql.connector.connect(
             user='root',
             password='123456',
             host='localhost',
             port=3306,
             db='cursos'
         )
      except Error as err:
         print("Error al intentar la conexión: {0}".format(err))
   
   # Metodo para mostrar cursos de base de datos
   def listarCursos(self):
      if self.conexion.is_connected():
         try:
            cursor = self.conexion.cursor()
            cursor.execute("SELECT * FROM cursos ORDER BY nombre ASC")
            resultado = cursor.fetchall()
            return resultado
         except Error as err:
            print("Error al intentar conectar: {0}".format(err))
   
   # Metodo para registrar curso en la base de datos
   def registrarCurso(self, curso):
      if self.conexion.is_connected():
         try:
            cursor = self.conexion.cursor()
            sql = "INSERT INTO cursos (codigo, nombre, creditos) VALUES ('{0}', '{1}', '{2}')"
            cursor.execute(sql.format(curso[0], curso[1], curso[2]))
            self.conexion.commit()
            print("\n> Curso Registrado <\n")
         except Error as err:
            print("Error al intentar la conexión: {0}".format(err))

   # Metodo para modificar un curso
   def actualizarCurso(self, curso):
      if self.conexion.is_connected():
         try:
            cursor = self.conexion.cursor()
            sql = "UPDATE cursos SET nombre = '{0}', creditos = {1} WHERE codigo = '{2}'"
            cursor.execute(sql.format(curso[1], curso[2], curso[0]))
            self.conexion.commit()
            print("\n> Curso actualizado <\n")

         except Error as err:
            print("Error al intentar la conexión: {0}".format(err))

   # Metodo para eliminar un curso de la base de datos
   def eliminarCurso(self, codigoEliminar):
      if self.conexion.is_connected():
         try:
            cursor = self.conexion.cursor()
            sql = "DELETE FROM cursos WHERE codigo = '{0}'"
            cursor.execute(sql.format(codigoEliminar))
            self.conexion.commit()
            print("\n> Curso eliminado <\n")
            
         except Error as err:
            print("Error al intentar la conexión: {0}".format(err))
