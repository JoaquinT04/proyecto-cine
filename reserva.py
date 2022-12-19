import tkinter as tk
from tkinter import ttk, Button, Frame, messagebox, Tk, Toplevel
from base_de_datos.BDD import crear_conexion, consulta, cerrar


class Vent_reserva(Toplevel):
    def __init__(self,root):
        super().__init__(root)
        self.root=root
        self.geometry("350x100")
        self.crear_widgets()
    
    def crear_widgets(self):
        ttk.Label(self, text="Ingrese ID de la funcion:").grid(row=1, column=0)
        ttk.Label(self, text="Ingrese numero de butaca:").grid(row=2, column=0)

        self.entry_ID = tk.StringVar()
        ttk.Entry(self, textvariable= self.entry_ID).grid(row=1, column=1)

        self.entry_butaca = tk.StringVar()
        ttk.Entry(self, textvariable= self.entry_butaca).grid(row=2, column=1)

        reservar = tk.Button(self, text="Reservar", command=lambda: reservar()).grid(row=1, column=2)
    
        def reservar():
            id = self.entry_ID.get()
            butaca = self.entry_butaca.get()
            conexion = crear_conexion()
            consulta_ = ""

    
