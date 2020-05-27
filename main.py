from tkinter import *
import tkinter as tk

from graficos import ParteGrafica
from dbquery import Consulta

class Main(ParteGrafica, Consulta):
    def __init__(self, root):
        root.resizable(0,0)
        #root.geometry('1024x720')
        root.title('Sistema de carga de recibos de sueldo')
        mainFrame = LabelFrame(root, text = 'Sistema de carga de recibos de sueldo')
        self.bg = 'seashell3'
        graficos = ParteGrafica(root) # Genera la parte grafica del Menú.
        consulta = Consulta() # Maneja los trabajos de consulta y escritura de la DB

if __name__ == '__main__':
    window = Tk()
    window.config(bg = 'seashell3')
    principal = Main(window)
    mainloop()