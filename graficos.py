from tkinter import *
import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *

from dbquery import Consulta

class ParteGrafica(Consulta): 
    def __init__(self, root):

        Consulta() # Llamo a la clase Consulta para poder usar sus metodos.

        self.mainRoot = root
        self.bg = 'seashell3'
        self.second_frame = LabelFrame(self.mainRoot, text = 'Manipulacion de datos', bg = self.bg) # Para cada division de la ventana creo un Frame.
        self.third_frame = LabelFrame(self.mainRoot, text = 'Lista de cargados', bg = self.bg)
        self.fourth_frame = LabelFrame(self.mainRoot, text = 'Mes mejor pago', bg = self.bg)#, height = 500, width = 500)

        # Grindeado de los Frames
        self.second_frame.grid(row = 0, column = 0, sticky = 'WENS')
        self.third_frame.grid(row = 0, column = 1, rowspan = 2, sticky = 'WENS')
        self.fourth_frame.grid(row = 1, column = 0, sticky = 'WENS')
        
        # Frame datos a cargar o Buscar
        
        botonCarga = Button(self.second_frame, text = 'Cargar', command = self.ventanaCarga)
        botonCarga.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'WENS')
        botonBusqueda = Button(self.second_frame, text = 'Buscar', command = self.ventanaVisualizarDatos)
        botonBusqueda.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'WENS')
        botonComparar = Button(self.second_frame, text = 'Comparar', command = self.seleccionParacomparar)
        botonComparar.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'WENS',)
    
        # Armado del Frame Treeview
        self.resumen = ttk.Treeview(self.third_frame, columns = ('#1', '#2'))

        self.resumen.column('#0', width=100, minwidth=20)
        self.resumen.column('#1', width=130, minwidth=100)
        self.resumen.column('#2', width=100, minwidth=100)

        self.resumen.heading('#0', text = 'Fecha')
        self.resumen.heading('#1', text = 'Sueldo')
        self.resumen.heading('#2', text = 'Hs totales')
        self.resumen.grid(row = 0, column = 0)

        scrollb = ttk.Scrollbar(self.third_frame)
        scrollb.grid(row = 0, column = 1, sticky = 'NS')
        self.poner_datos_ventana()
        
        # Armado del Frame Mes Mejor Pago

        mejormes = self.mejorMes() # Recibe los valres del mejor mes desde la DB.
        
        mejormesSumahs = mejormes[9] + mejormes[10] + mejormes[12]
        mejormesSumahs = str(round(mejormesSumahs, 2)) # Redondeo a 2 decimales.
        fechaMejormes = ('Fecha: %s' % (mejormes[6]))
        sueldoMejormes = ('Sueldo: %s' % (mejormes[32]))
        horasMejormes = ('Horas: %s' % (mejormesSumahs))

        # Si el total neto es el mas alto de la lista debera traer determinados valores de la tabla.
        Label(self.fourth_frame, text = fechaMejormes, bg = self.bg).grid(row = 0, column = 0, sticky = 'W')
        Label(self.fourth_frame, text = sueldoMejormes, bg = self.bg).grid(row = 1, column = 0, sticky = 'W')
        Label(self.fourth_frame, text = horasMejormes, bg = self.bg).grid(row = 2, column = 0, sticky = 'W')
        Label(self.fourth_frame, text = 'Feriado?: ', bg = self.bg).grid(row = 3, column = 0, sticky = 'W')
        Label(self.fourth_frame, text = 'Compensatorio?: ', bg = self.bg).grid(row = 4, column = 0, sticky = 'W')
        Label(self.fourth_frame, text = 'Premio?: ', bg = self.bg).grid(row = 5, column = 0, sticky = 'W')

        
        # Armado de el Menu Superior
        self.menubar = Menu(self.mainRoot)
        self.mainRoot.config(menu = self.menubar)  # Creacion de el Menu superior.

        self.filemenu = Menu(self.menubar)
        self.editmenu = Menu(self.menubar)
        self.helpmenu = Menu(self.menubar)

        self.menubar.add_cascade(label = "Archivo", menu = self.filemenu)
        self.menubar.add_cascade(label = "Editar", menu = self.editmenu)
        self.menubar.add_cascade(label = "Ayuda", menu = self.helpmenu)

    def poner_datos_ventana(self):
        # Limpiar tabla
        resultado_query = self.leerValores() # Traigo los valores desde la clase Consulta
        records = self.resumen.get_children() # Pongo a 0 la tabla para insertarle nuevos datos.
        for element in records:
            self.resumen.delete(element)
        # Trae todos los elementos de la tabla al treeview
        for x in resultado_query:
            #print(x)
            suma_hs = x[9] + x[10] + x[12]
            suma_hs = str(round(suma_hs, 2)) # Redondeo a 2 decimales.
            self.resumen.insert('', 0, text = x[6], values = (x[32], suma_hs))

    def ventanaCarga(self):
        
        # Creacion de los Frames
        self.nuevaVentana = Toplevel(bg = self.bg)
        frameTitulo = Frame(self.nuevaVentana, bg = self.bg)
        frameResumen = LabelFrame(self.nuevaVentana, text = 'Resumen', bg = self.bg)
        frameHaberes = LabelFrame(self.nuevaVentana, text = 'Haberes', bg = self.bg)
        frameDescuentos = LabelFrame(self.nuevaVentana, text = 'Descuentos', bg = self.bg)
        frameTotal = LabelFrame(self.nuevaVentana, text = 'Total', bg = self.bg)
        frameBotones = Frame(self.nuevaVentana, bg = self.bg)

        # Grideado de los Frames
        frameTitulo.grid(row = 0, column = 0, columnspan = 2, pady = 10, sticky = 'WNSE')
        frameResumen.grid(row = 1, column = 0, sticky = 'WNSE')
        frameHaberes.grid(row = 2, column = 0, sticky = 'WNSE')
        frameDescuentos.grid(row = 1, column = 1, sticky = 'WNSE')
        frameTotal.grid(row = 2, column = 1, sticky = 'WNSE')
        frameBotones.grid(row = 3, column = 0, columnspan = 2, pady = 10, sticky = 'WNSE')

        # Creacion Labels y boxes.
        def label(main, text, bg, row, column):
            label = Label(main, text = text, bg = bg)
            label.grid(row = row, column = column)

        def entry(main, row, column):
            entry = Entry(main)
            entry.grid(row = row, column = column)
            return entry

        Label(frameTitulo, text = 'Ventana de carga de datos', bg = self.bg, font = 20).pack()
        
        # Frame Resumen y
        label(frameResumen, 'Nombre', self.bg, 0, 0)
        self.valor0 = entry(frameResumen, 0, 1)
        self.valor0.focus()
        label(frameResumen, 'Categoria', self.bg, 1, 0)
        self.valor1 = entry(frameResumen, 1, 1)
        label(frameResumen, 'Basico $/h', self.bg, 2, 0)
        self.valor2 = entry(frameResumen, 2, 1)
        label(frameResumen, 'Antiguedad', self.bg, 3, 0)
        self.valor3 = entry(frameResumen, 3, 1)
        label(frameResumen, 'Antiguedad $/h', self.bg, 4, 0)
        self.valor4 = entry(frameResumen, 4, 1)
        label(frameResumen, 'Periodo', self.bg, 5, 0)
        self.valor5 = entry(frameResumen, 5, 1)
        label(frameResumen, 'Fecha de Pago', self.bg, 6, 0)
        self.valor6 = entry(frameResumen, 6, 1)
        label(frameResumen, 'Empresa', self.bg, 7, 0)
        self.valor7 = entry(frameResumen, 7, 1)

        # Frame Haberes
        label(frameHaberes, 'Sueldo basico', self.bg, 0, 0)
        self.valor8 = entry(frameHaberes, 0, 1)
        label(frameHaberes, 'Cantidad de HS', self.bg, 1, 0)
        self.valor9 = entry(frameHaberes, 1, 1)
        label(frameHaberes, 'Cant.HS Nocturnas', self.bg, 2, 0)
        self.valor10 = entry(frameHaberes, 2, 1)
        label(frameHaberes, '$ HS Nocturnas', self.bg, 3, 0)
        self.valor11 = entry(frameHaberes, 3, 1)
        label(frameHaberes, 'Cant.HS extras', self.bg, 4, 0)
        self.valor12 = entry(frameHaberes, 4, 1)
        label(frameHaberes, '$ HS extras diurnas', self.bg, 5 , 0)
        self.valor13 = entry(frameHaberes, 5, 1)
        label(frameHaberes, 'Premio Presentismo', self.bg, 6, 0)
        self.valor14 = entry(frameHaberes, 6, 1)
        label(frameHaberes, 'Adicional Puntualidad', self.bg, 7, 0)
        self.valor15 = entry(frameHaberes, 7, 1)
        label(frameHaberes, 'Adicional mod. trabajo', self.bg, 8, 0)
        self.valor16 = entry(frameHaberes, 8, 1)
        label(frameHaberes, 'Adicional GMB', self.bg, 9, 0)
        self.valor17 = entry(frameHaberes, 9, 1)
        label(frameHaberes, 'Aguinaldo', self.bg, 10, 0)
        self.valor18 = entry(frameHaberes, 10, 1)
        label(frameHaberes, 'Cierre de ejercicio', self.bg, 11, 0)
        self.valor19 = entry(frameHaberes, 11, 1)
        label(frameHaberes, 'Suma varios', self.bg, 12, 0)
        self.valor20 = entry(frameHaberes, 12, 1)
        label(frameHaberes, 'Haberes Varios', self.bg, 13, 0)
        self.valor21 = entry(frameHaberes, 13, 1)
        label(frameHaberes, 'Detalle haberes varios', self.bg, 14, 0)
        self.valor22 = entry(frameHaberes, 14, 1)
        
        # Frame Descuentos
        label(frameDescuentos, 'Gastos comida', self.bg, 0, 0)
        self.valor23 = entry(frameDescuentos, 0, 1)
        label(frameDescuentos, 'Obra Social', self.bg, 1, 0)
        self.valor24 = entry(frameDescuentos, 1, 1)
        label(frameDescuentos, 'Ley 19032', self.bg, 2, 0)
        self.valor25 = entry(frameDescuentos, 2, 1)
        label(frameDescuentos, 'Aporte Jubilatorio', self.bg, 3, 0)
        self.valor26 = entry(frameDescuentos, 3, 1)
        label(frameDescuentos, 'Impuesto a las ganancias', self.bg, 4, 0)
        self.valor27 = entry(frameDescuentos, 4, 1)
        label(frameDescuentos, 'Cuota Sindical', self.bg, 5, 0)
        self.valor28 = entry(frameDescuentos, 5, 1)
        label(frameDescuentos, 'Suma Varios', self.bg, 6, 0)
        self.valor29 = entry(frameDescuentos, 6, 1)
        label(frameDescuentos, 'Descuentos Varios', self.bg, 7, 0)
        self.valor30 = entry(frameDescuentos, 7, 1)
        label(frameDescuentos, 'Detalle descuentos varios', self.bg, 8, 0)
        self.valor31 = entry(frameDescuentos, 8, 1)

        # Frame Total
        label(frameTotal, 'Total neto', self.bg, 0, 0)
        self.valor32 = entry(frameTotal, 0, 1)

        # Botones
        botonCargar = Button(frameBotones, text = 'Cargar datos', command = self.cargarValores).pack()

    def cargarValores(self):
        mibase = mysql.connector.connect(
            host ='localhost',
            user = 'root',
            passwd = '',
            database = 'recibosdesueldo'
        )
        if self.valor6.get() == '':
            showerror ("Error", "No cargaste ningun dato")
            print('No se cargo la fecha')
        else:    
            micursor = mibase.cursor()
            datos = (self.valor0.get(), self.valor1.get(), self.valor2.get(), self.valor3.get(), self.valor4.get(), self.valor5.get(),
                    self.valor6.get(), self.valor7.get(), self.valor8.get(), self.valor9.get(), self.valor10.get(), self.valor11.get(), 
                    self.valor12.get(), self.valor13.get(), self.valor14.get(), self.valor15.get(), self.valor16.get(), self.valor17.get(), self.valor18.get(), 
                    self.valor19.get(), self.valor20.get(), self.valor21.get(), self.valor22.get(), self.valor23.get(), self.valor24.get(), self.valor25.get(), 
                    self.valor26.get(), self.valor27.get(), self.valor28.get(), self.valor29.get(), self.valor30.get(), self.valor31.get(), self.valor32.get())
            sql = '''INSERT INTO datos_mes (nombre, categoria, basico_precio, antiguedad, antiguedad_precio, periodo, fecha_pago, empresa, sueldo_basico,cantidad_hs,
                    cant_hs_noct,precio_hs_noct,cant_hs_extras,precio_hs_extras,premio_presentismo,adicional_punt,adicional_mod_trabajo,adicional_gmb,aguinaldo,cierre_ejercicio,
                    suma_varios,haberes_varios,detalle_haberes_varios,gastos_comida,obra_social,ley_19032,aporte_jubilatorio,imp_ganancias,cuota_sindical,suma_varios_dsc,
                    descuentos_varios,detalle_desc_varios,total_neto) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

            micursor.execute(sql, datos)
            mibase.commit()
            self.poner_datos_ventana()
            self.nuevaVentana.destroy()

    def ventanaVisualizarDatos(self):
        # Creacion de los Frames
        self.VisualizarDatos = Toplevel(bg = self.bg)
        frameTitulo = Frame(self.VisualizarDatos, bg = self.bg)
        frameResumen = LabelFrame(self.VisualizarDatos, text = 'Resumen', bg = self.bg)
        frameHaberes = LabelFrame(self.VisualizarDatos, text = 'Haberes', bg = self.bg)
        frameDescuentos = LabelFrame(self.VisualizarDatos, text = 'Descuentos', bg = self.bg)
        frameTotal = LabelFrame(self.VisualizarDatos, text = 'Total', bg = self.bg)
        frameBotones = Frame(self.VisualizarDatos, bg = self.bg)

         # Grideado de los Frames
        frameTitulo.grid(row = 0, column = 0, columnspan = 2, pady = 10, sticky = 'WNSE')
        frameResumen.grid(row = 1, column = 0, sticky = 'WNSE')
        frameHaberes.grid(row = 2, column = 0, sticky = 'WNSE')
        frameDescuentos.grid(row = 1, column = 1, sticky = 'WNSE')
        frameTotal.grid(row = 2, column = 1, sticky = 'WNSE')
        frameBotones.grid(row = 3, column = 0, columnspan = 2, pady = 10, sticky = 'WNSE')

        # Creacion Labels y boxes.
        def label(main, text, bg, row, column):
            label = Label(main, text = text, bg = bg)
            label.grid(row = row, column = column)

        #Invoca funcion para cargar todos los valores de la consulta seleccionada en el treeview.
        resultado = self.traerValores()
        
        Label(frameTitulo, text = 'Visualizacion de datos', bg = self.bg, font = 20).pack()

        # Frame Resumen 
        label(frameResumen, 'Nombre:', self.bg, 0, 0)
        label(frameResumen, resultado[0], self.bg, 0, 1)
        label(frameResumen, 'Categoria:', self.bg, 1, 0)
        label(frameResumen, resultado[1], self.bg, 1, 1)
        label(frameResumen, 'Basico $/h:', self.bg, 2, 0)
        label(frameResumen, resultado[2], self.bg, 2, 1)
        label(frameResumen, 'Antiguedad:', self.bg, 3, 0)
        label(frameResumen, resultado[3], self.bg, 3, 1)
        label(frameResumen, 'Antiguedad $/h:', self.bg, 4, 0)
        label(frameResumen, resultado[4], self.bg, 4, 1)
        label(frameResumen, 'Periodo:', self.bg, 5, 0)
        label(frameResumen, resultado[5], self.bg, 5, 1)
        label(frameResumen, 'Fecha de Pago:', self.bg, 6, 0)
        label(frameResumen, resultado[6], self.bg, 6, 1)
        label(frameResumen, 'Empresa:', self.bg, 7, 0)
        label(frameResumen, resultado[7], self.bg, 7, 1)

        # Frame Haberes
        label(frameHaberes, 'Sueldo basico:', self.bg, 0, 0)
        label(frameHaberes, resultado[8], self.bg, 0, 1)
        label(frameHaberes, 'Cantidad de HS:', self.bg, 1, 0)
        label(frameHaberes, resultado[9], self.bg, 1, 1)
        label(frameHaberes, 'Cant.HS Nocturnas:', self.bg, 2, 0)
        label(frameHaberes, resultado[10], self.bg, 2, 1)
        label(frameHaberes, '$ HS Nocturnas:', self.bg, 3, 0)
        label(frameHaberes, resultado[11], self.bg, 3, 1)
        label(frameHaberes, 'Cant.HS extras:', self.bg, 4, 0)
        label(frameHaberes, resultado[12], self.bg, 4, 1)
        label(frameHaberes, '$ HS extras diurnas:', self.bg, 5 , 0)
        label(frameHaberes, resultado[13], self.bg, 5 , 1)
        label(frameHaberes, 'Premio Presentismo:', self.bg, 6, 0)
        label(frameHaberes, resultado[14], self.bg, 6, 1)
        label(frameHaberes, 'Adicional Puntualidad:', self.bg, 7, 0)
        label(frameHaberes, resultado[15], self.bg, 7, 1)
        label(frameHaberes, 'Adicional mod. trabajo:', self.bg, 8, 0)
        label(frameHaberes, resultado[16], self.bg, 8, 1)
        label(frameHaberes, 'Adicional GMB:', self.bg, 9, 0)
        label(frameHaberes, resultado[17], self.bg, 9, 1)
        label(frameHaberes, 'Aguinaldo:', self.bg, 10, 0)
        label(frameHaberes, resultado[18], self.bg, 10, 1)
        label(frameHaberes, 'Cierre de ejercicio:', self.bg, 11, 0)
        label(frameHaberes, resultado[19], self.bg, 11, 1)
        label(frameHaberes, 'Suma varios:', self.bg, 12, 0)
        label(frameHaberes, resultado[20], self.bg, 12, 1)
        label(frameHaberes, 'Haberes Varios:', self.bg, 13, 0)
        label(frameHaberes, resultado[21], self.bg, 13, 1)
        label(frameHaberes, 'Detalle haberes varios:', self.bg, 14, 0)
        label(frameHaberes, resultado[22], self.bg, 14, 1)
        
        # Frame Descuentos
        label(frameDescuentos, 'Gastos comida:', self.bg, 0, 0)
        label(frameDescuentos, resultado[23], self.bg, 0, 1)
        label(frameDescuentos, 'Obra Social:', self.bg, 1, 0)
        label(frameDescuentos, resultado[24], self.bg, 1, 1)
        label(frameDescuentos, 'Ley 19032:', self.bg, 2, 0)
        label(frameDescuentos, resultado[25], self.bg, 2, 1)
        label(frameDescuentos, 'Aporte Jubilatorio:', self.bg, 3, 0)
        label(frameDescuentos, resultado[26], self.bg, 3, 1)
        label(frameDescuentos, 'Impuesto a las ganancias:', self.bg, 4, 0)
        label(frameDescuentos, resultado[27], self.bg, 4, 1)
        label(frameDescuentos, 'Cuota Sindical:', self.bg, 5, 0)
        label(frameDescuentos, resultado[28], self.bg, 5, 1)
        label(frameDescuentos, 'Suma Varios:', self.bg, 6, 0)
        label(frameDescuentos, resultado[29], self.bg, 6, 1)
        label(frameDescuentos, 'Descuentos Varios:', self.bg, 7, 0)
        label(frameDescuentos, resultado[30], self.bg, 7, 1)
        label(frameDescuentos, 'Detalle descuentos varios:', self.bg, 8, 0)
        label(frameDescuentos, resultado[31], self.bg, 8, 1)

        # Frame Total
        label(frameTotal, 'Total neto:', self.bg, 0, 0)
        label(frameTotal, resultado[32], self.bg, 0, 1)

        # Botones
        botonSalir = Button(frameBotones, text = 'Salir', command = self.VisualizarDatos.destroy).pack()

    def apretarBoton(self, par1 = '', par2 = ''):
        self.resultado = self.traerParacomparar(par1, par2)
        self.ventanaComparacion()        

    def seleccionParacomparar(self):
        if (self.resumen.item(self.resumen.selection())['text']) == '':
            showerror ("Error", "No se seleccion una carga")
            print('No se seleccion una carga')
        else:
            self.frame = Toplevel(bg = self.bg)

            frame1 = Frame(self.frame, bg = self.bg)
            frame1.grid(row = 0, column = 0)
            frame2 = Frame(self.frame, bg = self.bg)
            frame2.grid(row = 1, column = 0)

            self.fechaSeleccionada = self.resumen.item(self.resumen.selection())['text']
            Label(frame1, text = 'Mes seleccionado', bg = self.bg).grid(row = 0, column = 0)
            Label(frame1, text = self.fechaSeleccionada, bg = self.bg).grid(row = 0, column = 1)
            Label(frame1, text = 'Fecha a comparar', bg = self.bg).grid(row = 1, column = 0)
            self.fechaAcomparar = Entry(frame1)
            self.fechaAcomparar.grid(row = 1, column = 1)
            
            Button(frame1, text = 'Comparar', command = lambda: self.apretarBoton(self.fechaAcomparar.get(),self.fechaSeleccionada)).grid(row = 2, column = 0, columnspan = 2, pady = 5)
            
    def ventanaComparacion(self):

        # Creacion de frames
        frame2 = Frame(self.frame, bg = self.bg)
        frame2.grid(row = 3, column = 0)
        frameTitulo = Frame(frame2, bg = self.bg)
        frameResumen = LabelFrame(frame2, text = 'Resumen', bg = self.bg)
        frameHaberes = LabelFrame(frame2, text = 'Haberes', bg = self.bg)
        frameDescuentos = LabelFrame(frame2, text = 'Descuentos', bg = self.bg)
        frameTotal = LabelFrame(frame2, text = 'Total', bg = self.bg)
        
         # Grideado de los Frames
        frameTitulo.grid(row = 0, column = 0, columnspan = 2, pady = 10, sticky = 'WNSE')
        frameResumen.grid(row = 1, column = 0, sticky = 'WNSE')
        frameHaberes.grid(row = 2, column = 0, sticky = 'WNSE')
        frameDescuentos.grid(row = 1, column = 1, sticky = 'WNSE')
        frameTotal.grid(row = 2, column = 1, sticky = 'WNSE')
        

        # Creacion Labels y boxes.
        def label(main, text, bg, row, column):
            label = Label(main, text = text, bg = bg)
            label.grid(row = row, column = column)

        def label2(main, text, bg, row, column):
            label = Label(main, text = text, bg = bg, fg = 'red')
            label.grid(row = row, column = column)

        resultado1 = self.resultado[1]
        resultado2 = self.resultado[0]
      
        # Frame Titulo
        Label(frameTitulo, text = 'Ventana de comparacion de datos', bg = self.bg, font = 20).pack()

        # Frame Resumen 
        label(frameResumen, 'Nombre:', self.bg, 0, 0)
        label(frameResumen, resultado1[0], self.bg, 0, 1)
        label2(frameResumen, resultado2[0], self.bg, 0, 2)
        label(frameResumen, 'Categoria:', self.bg, 1, 0)
        label(frameResumen, resultado1[1], self.bg, 1, 1)
        label2(frameResumen, resultado2[1], self.bg, 1, 2)
        label(frameResumen, 'Basico $/h:', self.bg, 2, 0)
        label(frameResumen, resultado1[2], self.bg, 2, 1)
        label2(frameResumen, resultado2[2], self.bg, 2, 2)
        label(frameResumen, 'Antiguedad:', self.bg, 3, 0)
        label(frameResumen, resultado1[3], self.bg, 3, 1)
        label2(frameResumen, resultado2[3], self.bg, 3, 2)
        label(frameResumen, 'Antiguedad $/h:', self.bg, 4, 0)
        label(frameResumen, resultado1[4], self.bg, 4, 1)
        label2(frameResumen, resultado2[4], self.bg, 4, 2)
        label(frameResumen, 'Periodo:', self.bg, 5, 0)
        label(frameResumen, resultado1[5], self.bg, 5, 1)
        label2(frameResumen, resultado2[5], self.bg, 5, 2)
        label(frameResumen, 'Fecha de Pago:', self.bg, 6, 0)
        label(frameResumen, resultado1[6], self.bg, 6, 1)
        label2(frameResumen, resultado2[6], self.bg, 6, 2)
        label(frameResumen, 'Empresa:', self.bg, 7, 0)
        label(frameResumen, resultado1[7], self.bg, 7, 1)
        label2(frameResumen, resultado2[7], self.bg, 7, 2)

        # Frame Haberes
        label(frameHaberes, 'Sueldo basico:', self.bg, 0, 0)
        label(frameHaberes, resultado1[8], self.bg, 0, 1)
        label2(frameHaberes, resultado2[8], self.bg, 0, 2)
        label(frameHaberes, 'Cantidad de HS:', self.bg, 1, 0)
        label(frameHaberes, resultado1[9], self.bg, 1, 1)
        label2(frameHaberes, resultado2[9], self.bg, 1, 2)
        label(frameHaberes, 'Cant.HS Nocturnas:', self.bg, 2, 0)
        label(frameHaberes, resultado1[10], self.bg, 2, 1)
        label2(frameHaberes, resultado2[10], self.bg, 2, 2)
        label(frameHaberes, '$ HS Nocturnas:', self.bg, 3, 0)
        label(frameHaberes, resultado1[11], self.bg, 3, 1)
        label2(frameHaberes, resultado2[11], self.bg, 3, 2)
        label(frameHaberes, 'Cant.HS extras:', self.bg, 4, 0)
        label(frameHaberes, resultado1[12], self.bg, 4, 1)
        label2(frameHaberes, resultado2[12], self.bg, 4, 2)
        label(frameHaberes, '$ HS extras diurnas:', self.bg, 5 , 0)
        label(frameHaberes, resultado1[13], self.bg, 5 , 1)
        label2(frameHaberes, resultado2[13], self.bg, 5 , 2)
        label(frameHaberes, 'Premio Presentismo:', self.bg, 6, 0)
        label(frameHaberes, resultado1[14], self.bg, 6, 1)
        label2(frameHaberes, resultado2[14], self.bg, 6, 2)
        label(frameHaberes, 'Adicional Puntualidad:', self.bg, 7, 0)
        label(frameHaberes, resultado1[15], self.bg, 7, 1)
        label2(frameHaberes, resultado2[15], self.bg, 7, 2)
        label(frameHaberes, 'Adicional mod. trabajo:', self.bg, 8, 0)
        label(frameHaberes, resultado1[16], self.bg, 8, 1)
        label2(frameHaberes, resultado2[16], self.bg, 8, 2)
        label(frameHaberes, 'Adicional GMB:', self.bg, 9, 0)
        label(frameHaberes, resultado1[17], self.bg, 9, 1)
        label2(frameHaberes, resultado2[17], self.bg, 9, 2)
        label(frameHaberes, 'Aguinaldo:', self.bg, 10, 0)
        label(frameHaberes, resultado1[18], self.bg, 10, 1)
        label2(frameHaberes, resultado2[18], self.bg, 10, 2)
        label(frameHaberes, 'Cierre de ejercicio:', self.bg, 11, 0)
        label(frameHaberes, resultado1[19], self.bg, 11, 1)
        label2(frameHaberes, resultado2[19], self.bg, 11, 2)
        label(frameHaberes, 'Suma varios:', self.bg, 12, 0)
        label(frameHaberes, resultado1[20], self.bg, 12, 1)
        label2(frameHaberes, resultado2[20], self.bg, 12, 2)
        label(frameHaberes, 'Haberes Varios:', self.bg, 13, 0)
        label(frameHaberes, resultado1[21], self.bg, 13, 1)
        label2(frameHaberes, resultado2[21], self.bg, 13, 2)
        label(frameHaberes, 'Detalle haberes varios:', self.bg, 14, 0)
        label(frameHaberes, resultado1[22], self.bg, 14, 1)
        label2(frameHaberes, resultado2[22], self.bg, 14, 2)
        
        # Frame Descuentos
        label(frameDescuentos, 'Gastos comida:', self.bg, 0, 0)
        label(frameDescuentos, resultado1[23], self.bg, 0, 1)
        label2(frameDescuentos, resultado2[23], self.bg, 0, 2)
        label(frameDescuentos, 'Obra Social:', self.bg, 1, 0)
        label(frameDescuentos, resultado1[24], self.bg, 1, 1)
        label2(frameDescuentos, resultado2[24], self.bg, 1, 2)
        label(frameDescuentos, 'Ley 19032:', self.bg, 2, 0)
        label(frameDescuentos, resultado1[25], self.bg, 2, 1)
        label2(frameDescuentos, resultado2[25], self.bg, 2, 2)
        label(frameDescuentos, 'Aporte Jubilatorio:', self.bg, 3, 0)
        label(frameDescuentos, resultado1[26], self.bg, 3, 1)
        label2(frameDescuentos, resultado2[26], self.bg, 3, 2)
        label(frameDescuentos, 'Impuesto a las ganancias:', self.bg, 4, 0)
        label(frameDescuentos, resultado1[27], self.bg, 4, 1)
        label2(frameDescuentos, resultado2[27], self.bg, 4, 2)
        label(frameDescuentos, 'Cuota Sindical:', self.bg, 5, 0)
        label(frameDescuentos, resultado1[28], self.bg, 5, 1)
        label2(frameDescuentos, resultado2[28], self.bg, 5, 2)
        label(frameDescuentos, 'Suma Varios:', self.bg, 6, 0)
        label(frameDescuentos, resultado1[29], self.bg, 6, 1)
        label2(frameDescuentos, resultado2[29], self.bg, 6, 2)
        label(frameDescuentos, 'Descuentos Varios:', self.bg, 7, 0)
        label(frameDescuentos, resultado1[30], self.bg, 7, 1)
        label2(frameDescuentos, resultado2[30], self.bg, 7, 2)
        label(frameDescuentos, 'Detalle descuentos varios:', self.bg, 8, 0)
        label(frameDescuentos, resultado1[31], self.bg, 8, 1)
        label2(frameDescuentos, resultado2[31], self.bg, 8, 2)

        # Frame Total
        label(frameTotal, 'Total neto:', self.bg, 0, 0)
        label(frameTotal, resultado1[32], self.bg, 0, 1)
        label2(frameTotal, resultado2[32], self.bg, 0, 2)

if __name__ == '__main__':

    window = Tk()
    principal = ParteGrafica(window)
    mainloop()
