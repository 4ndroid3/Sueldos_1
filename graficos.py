from tkinter import *
import tkinter as tk
from tkinter import ttk

from dbquery import Consulta

class ParteGrafica(Consulta): 
    def __init__(self, root):

        Consulta() # Llamo a la clase Consulta para poder usar sus metodos.

        self.mainRoot = root
        self.bg = 'seashell3'
        self.second_frame = LabelFrame(self.mainRoot, text = 'Carga de datos', bg = self.bg) # Para cada division de la ventana creo un Frame.
        self.third_frame = LabelFrame(self.mainRoot, text = 'Lista de cargados', bg = self.bg)
        self.fourth_frame = LabelFrame(self.mainRoot, text = 'Mes mejor pago', bg = self.bg, height = 500, width = 500)

        # Grindeado de los Frames
        self.second_frame.grid(row = 0, column = 0, sticky = 'NS')
        self.third_frame.grid(row = 0, column = 1, rowspan = 2, sticky = 'NS')
        self.fourth_frame.grid(row = 1, column = 0, sticky = 'NS')
        
        # Frame datos a cargar o Buscar
        
        search_text1 = Label(self.second_frame, text = 'Año:', bg = self.bg)
        search_text1.grid(row = 1, column = 0) # Dentro del frame organizo con Grid todos los elementos incluidos en el Frame.
        search_box1 = Entry(self.second_frame)
        search_box1.focus()
        search_box1.grid(row = 1, column = 1, padx = 5)

        search_text2 = Label(self.second_frame, text = 'Mes:', bg = self.bg)
        search_text2.grid(row = 2, column = 0)
        search_box2 = Entry(self.second_frame)
        search_box2.grid(row = 2, column = 1, padx = 5)

        # Frame aparte para dejar botones centrados
        frameBotones = Frame(self.second_frame, bg = self.bg)
        frameBotones.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5)
       
        botonCarga = Button(frameBotones, text = 'Cargar', command = self.ventanaCarga)
        botonCarga.grid(row = 0, column = 0, padx = 5, pady = 5)
        botonBusqueda = Button(frameBotones, text = 'Buscar')
        botonBusqueda.grid(row = 0, column = 1, padx = 5, pady = 5)
    
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
        # Si el total neto es el mas alto de la lista debera traer determinados valores de la tabla.
        Label(self.fourth_frame, text = 'Fecha: ', bg = self.bg).grid(row = 0, column = 0, sticky = 'W')
        Label(self.fourth_frame, text = 'Sueldo: ', bg = self.bg).grid(row = 1, column = 0, sticky = 'W')
        Label(self.fourth_frame, text = 'Horas: ', bg = self.bg).grid(row = 1, column = 1, sticky = 'W')
        Label(self.fourth_frame, text = 'Feriado?: ', bg = self.bg).grid(row = 2, column = 1, sticky = 'W')
        Label(self.fourth_frame, text = 'Compensatorio?: ', bg = self.bg).grid(row = 2, column = 0, sticky = 'W')
        Label(self.fourth_frame, text = 'Premio?: ', bg = self.bg).grid(row = 2, column = 1, sticky = 'W')
        
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
            print(x)
            suma_hs = x[9] + x[10] + x[11]
            suma_hs = str(round(suma_hs, 2)) # Redondeo a 2 decimales.
            self.resumen.insert('', 0, text = x[6], values = (x[32], suma_hs))

    def ventanaCarga(self):
        
        # Creacion de los Frames
        nuevaVentana = Toplevel(bg = self.bg)
        frameTitulo = Frame(nuevaVentana, bg = self.bg)
        frameResumen = LabelFrame(nuevaVentana, text = 'Resumen', bg = self.bg)
        frameHaberes = LabelFrame(nuevaVentana, text = 'Haberes', bg = self.bg)
        frameDescuentos = LabelFrame(nuevaVentana, text = 'Descuentos', bg = self.bg)
        frameTotal = LabelFrame(nuevaVentana, text = 'Total', bg = self.bg)
        frameBotones = Frame(nuevaVentana, bg = self.bg)

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
        
        # Frame Resumen
        label(frameResumen, 'Nombre', self.bg, 0, 0)
        valor0 = entry(frameResumen, 0, 1)
        label(frameResumen, 'Categoria', self.bg, 1, 0)
        valor1 = entry(frameResumen, 1, 1)
        label(frameResumen, 'Basico $/h', self.bg, 2, 0)
        valor2 = entry(frameResumen, 2, 1)
        label(frameResumen, 'Antiguedad', self.bg, 3, 0)
        valor3 = entry(frameResumen, 3, 1)
        label(frameResumen, 'Antiguedad $/h', self.bg, 4, 0)
        valor4 = entry(frameResumen, 4, 1)
        label(frameResumen, 'Periodo', self.bg, 5, 0)
        valor5 = entry(frameResumen, 5, 1)
        label(frameResumen, 'Fecha de Pago', self.bg, 6, 0)
        valor6 = entry(frameResumen, 6, 1)
        label(frameResumen, 'Empresa', self.bg, 7, 0)
        valor7 = entry(frameResumen, 7, 1)

        # Frame Haberes
        label(frameHaberes, 'Sueldo basico', self.bg, 0, 0)
        valor8 = entry(frameHaberes, 0, 1)
        label(frameHaberes, 'Cantidad de HS', self.bg, 1, 0)
        valor9 = entry(frameHaberes, 1, 1)
        label(frameHaberes, 'Cant.HS Nocturnas', self.bg, 2, 0)
        valor10 = entry(frameHaberes, 2, 1)
        label(frameHaberes, '$ HS Nocturnas', self.bg, 3, 0)
        valor11 = entry(frameHaberes, 3, 1)
        label(frameHaberes, 'Cant.HS extras', self.bg, 4, 0)
        valor12 = entry(frameHaberes, 4, 1)
        label(frameHaberes, '$ HS extras diurnas', self.bg, 5 , 0)
        valor13 = entry(frameHaberes, 5, 1)
        label(frameHaberes, 'Premio P¨resentismo', self.bg, 6, 0)
        valor14 = entry(frameHaberes, 6, 1)
        label(frameHaberes, 'Adicional Puntualidad', self.bg, 7, 0)
        valor15 = entry(frameHaberes, 7, 1)
        label(frameHaberes, 'Adicional mod. trabajo', self.bg, 8, 0)
        valor16 = entry(frameHaberes, 8, 1)
        label(frameHaberes, 'Adicional GMB', self.bg, 9, 0)
        valor17 = entry(frameHaberes, 9, 1)
        label(frameHaberes, 'Aguinaldo', self.bg, 10, 0)
        valor18 = entry(frameHaberes, 10, 1)
        label(frameHaberes, 'Cierre de ejercicio', self.bg, 11, 0)
        valor19 = entry(frameHaberes, 11, 1)
        label(frameHaberes, 'Suma varios', self.bg, 12, 0)
        valor20 = entry(frameHaberes, 12, 1)
        label(frameHaberes, 'Haberes Varios', self.bg, 13, 0)
        valor21 = entry(frameHaberes, 13, 1)
        label(frameHaberes, 'Detalle haberes varios', self.bg, 14, 0)
        valor22 = entry(frameHaberes, 14, 1)
        
        # Frame Descuentos
        label(frameDescuentos, 'Gastos comida', self.bg, 0, 0)
        valor23 = entry(frameDescuentos, 0, 1)
        label(frameDescuentos, 'Obra Social', self.bg, 1, 0)
        valor24 = entry(frameDescuentos, 1, 1)
        label(frameDescuentos, 'Ley 19032', self.bg, 2, 0)
        valor25 = entry(frameDescuentos, 2, 1)
        label(frameDescuentos, 'Aporte Jubilatorio', self.bg, 3, 0)
        valor26 = entry(frameDescuentos, 3, 1)
        label(frameDescuentos, 'Impuesto a las ganancias', self.bg, 4, 0)
        valor27 = entry(frameDescuentos, 4, 1)
        label(frameDescuentos, 'Cuota Sindical', self.bg, 5, 0)
        valor28 = entry(frameDescuentos, 5, 1)
        label(frameDescuentos, 'Suma Varios', self.bg, 6, 0)
        valor29 = entry(frameDescuentos, 6, 1)
        label(frameDescuentos, 'Descuentos Varios', self.bg, 7, 0)
        valor30 = entry(frameDescuentos, 7, 1)
        label(frameDescuentos, 'Detalle descuentos varios', self.bg, 8, 0)
        valor31 = entry(frameDescuentos, 8, 1)

        # Frame Total
        label(frameTotal, 'Total neto', self.bg, 0, 0)
        valor32 = entry(frameTotal, 0, 1)

        # Botones
        botonCargar = Button(frameBotones, text = 'Cargar datos').pack()
        

if __name__ == '__main__':

    window = Tk()
    principal = ParteGrafica(window)
    mainloop()
