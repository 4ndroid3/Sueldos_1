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
       
        botonCarga = Button(frameBotones, text = 'Cargar')
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
        for x in resultado_query:
            print(x)
            suma_hs = x[8] + x[9] + x[11]
            self.resumen.insert('', 0, text = x[6], values = (x[31], suma_hs))

    def ventanaCarga(self):
        nuevaVentana = Toplevel()
    
        
        
        

if __name__ == '__main__':

    window = Tk()
    principal = ParteGrafica(window)
    mainloop()
