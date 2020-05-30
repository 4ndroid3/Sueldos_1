import mysql.connector # Importo el conector de MySQL

class Consulta:
    def __init__(self):
        
        """while True:
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
                    break"""
    
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

    def traerValores(self):
        mibase = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            passwd = '',
            database = 'recibosdesueldo'
        )
        micursor = mibase.cursor()
        fechaBusqueda = self.resumen.item(self.resumen.selection())['text'] # Renglon del treeview seleccionado con el mouse.
        sql = ('SELECT * FROM datos_mes WHERE fecha_pago = %s')
        datos = (fechaBusqueda, ) # En los datos siempre se debe entregar una tupla, por eso se pone el valor y dsp ","
        micursor.execute(sql, datos)
        listaResultado = micursor.fetchall()
        resultado = listaResultado[0] # El comando fetchall devuelve una lista que en su primer valor tiene una tupla con todos los resultados.
        
        return resultado

    def mejorMes(self):
        mibase = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            passwd = '',
            database = 'recibosdesueldo'
        )
        micursor = mibase.cursor()
        sql = 'SELECT * FROM datos_mes WHERE total_neto = (SELECT MAX(total_neto) FROM datos_mes)'
        micursor.execute(sql)
        listaResultado = micursor.fetchall()
        resultado = listaResultado[0] # El comando fetchall devuelve una lista que en su primer valor tiene una tupla con todos los resultados.
        
        return resultado

    def traerParacomparar(self, mesAcomparar = '', mesAcomparar1 = ''):
            mibase = mysql.connector.connect(
                host ='localhost',
                user = 'root',
                passwd = '',
                database = 'recibosdesueldo'
            )
            micursor = mibase.cursor()
            sql = ('SELECT * FROM datos_mes WHERE (fecha_pago = %s) OR (fecha_pago = %s)')
            datos = (mesAcomparar, mesAcomparar1) # En los datos siempre se debe entregar una tupla, por eso se pone el valor y dsp ","
            micursor.execute(sql, datos)
            listaResultado = micursor.fetchall()
            resultado = listaResultado # El comando fetchall devuelve una lista que en su primer valor tiene una tupla con todos los resultados.
            
            return resultado