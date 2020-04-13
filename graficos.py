from tkinter import *
import tkinter as tk
from tkinter import ttk


class Carga: 
    def __init__(self, root):

        self.second_frame = LabelFrame(root, text = 'Carga de datos') # Para cada division de la ventana creo un Frame.
        search_text1 = Label(self.second_frame, text = 'Año:')
        search_text1.grid(row = 1, column = 0) # Dentro del frame organizo con Grid todos los elementos incluidos en el Frame.
        search_box1 = Entry(self.second_frame)
        search_box1.focus()
        search_box1.grid(row = 1, column = 1, padx = 5)

        search_text2 = Label(self.second_frame, text = 'Mes:')
        search_text2.grid(row = 2, column = 0)
        search_box2 = Entry(self.second_frame)
        search_box2.grid(row = 2, column = 1, padx = 5)

        # Frame aparte para dejar botones centrados
        frameBotones = Frame(self.second_frame)
        frameBotones.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5)

       
        botonCarga = Button(frameBotones, text = 'Cargar')
        botonCarga.grid(row = 0, column = 0, padx = 5, pady = 5)
        botonBusqueda = Button(frameBotones, text = 'Buscar')
        botonBusqueda.grid(row = 0, column = 1, padx = 5, pady = 5)
        # -----------------------------------------
class Listacargados:
    
    def __init__(self, root):
        self.third_frame = LabelFrame(root, text = 'Lista de cargados')
        resumen = ttk.Treeview(self.third_frame, columns = ('fecha', 'sueldo'))

        resumen.column('#0', width=40, minwidth=20)
        resumen.column('fecha', width=130, minwidth=100)
        resumen.column('sueldo', width=130, minwidth=100)

        resumen.heading('#0', text = 'N°')
        resumen.heading('fecha', text = 'Fecha')
        resumen.heading('sueldo', text = 'Sueldo')
        resumen.grid(row = 0, column = 0)



        scrollb = ttk.Scrollbar(self.third_frame)
        scrollb.grid(row = 0, column = 1, sticky = 'NS')
class Mejorpago():
    def __init__(self, root):
        self.fourth_frame = LabelFrame(root, text = 'Mes mejor pago')
        Label(self.fourth_frame, text = 'Fecha: ').grid(row = 0, column = 0, sticky = 'W')
        Label(self.fourth_frame, text = 'Sueldo: ').grid(row = 1, column = 0, sticky = 'W')
        Label(self.fourth_frame, text = 'Horas: ').grid(row = 1, column = 1, sticky = 'W')
        Label(self.fourth_frame, text = 'Feriado?: ').grid(row = 2, column = 1, sticky = 'W')
        Label(self.fourth_frame, text = 'Compensatorio?: ').grid(row = 2, column = 0, sticky = 'W')
        Label(self.fourth_frame, text = 'Premio?: ').grid(row = 2, column = 1, sticky = 'W')
class Menusup():
    def __init__(self, root):
        self.menubar = Menu(root)
        root.config(menu = self.menubar)  # Creacion de el Menu superior.

        self.filemenu = Menu(self.menubar)
        self.editmenu = Menu(self.menubar)
        self.helpmenu = Menu(self.menubar)

        self.menubar.add_cascade(label="Archivo", menu=self.filemenu)
        self.menubar.add_cascade(label="Editar", menu=self.editmenu)
        self.menubar.add_cascade(label="Ayuda", menu=self.helpmenu)

if __name__ == '__main__':

    window = Tk()
    principal = Carga(window)
    mainloop()
