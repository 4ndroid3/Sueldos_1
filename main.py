from tkinter import *
import tkinter as tk

from graficos import Carga
from graficos import Listacargados
from graficos import Mejorpago
from graficos import Menusup

class Main(Carga, Listacargados, Mejorpago, Menusup):
    def __init__(self, root):
        root.title('Sistema de carga de recibos de sueldo')
        mainFrame = LabelFrame(root, text = 'Sistema de carga de recibos de sueldo')

        frame1 = Carga(root)
        frame2 = Listacargados(root)
        frame3 = Mejorpago(root)
        frame4 = Menusup(root)

        frame1.second_frame.grid(row = 0, column = 0, sticky = 'WENS')
        frame2.third_frame.grid(row = 0, column = 1, rowspan = 2, sticky = 'WENS')
        frame3.fourth_frame.grid(row = 1, column = 0, sticky = 'WENS')
        

if __name__ == '__main__':
    window = Tk()
    principal = Main(window)
    mainloop()