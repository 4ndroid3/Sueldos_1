import mysql.connector # Importo el conector de MySQL

class Consulta:
    def __init__(self):
        
        while True:
                try:
                    mibase = mysql.connector.connect(
                        host ='localhost',
                        user = 'root',
                        passwd = ''
                    )
                    micursor = mibase.cursor()
                    micursor.execute('CREATE DATABASE recibosdesueldo') # la tabla es 'datos_mes'
                    print('Base de datos creada con Exito')
                    break
                except mysql.connector.errors.DatabaseError: # En la excepcion pongo el error de base de datos ya creada.
                    print('La base de datos ya está creada')
                    #self.mensaje['text'] = 'La Base de Datos ya está creada.'
                    break
    
    def leerValores(self):
        mibase = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            passwd = '',
            database = 'recibosdesueldo'
        )
        micursor = mibase.cursor()
        sql = 'SELECT * FROM datos_mes'
        micursor.execute(sql)
        resultado = micursor.fetchall() # Devuelve una lista de Tuplas con los datos.
        
        return resultado