import tkinter as tk
from tkinter import ttk, Button, Frame, messagebox, Tk, Toplevel
from base_de_datos.BDD import crear_conexion, consulta
from BDD.consulta_producto import select_producto#, select_producto_by_id
#from BDD.insertar_datos import crear_datos
from clases.Sala import Sala

class Cliente(Toplevel):
    def __init__(self,root):
        super().__init__(root)
        self.root=root
        self.geometry("960x600")
        self._create_label_input()

    def _create_label_input(self):
        form_frame = tk.Frame(self)
        form_frame.pack()

        sala = Sala()
        conexion = crear_conexion()
        consulta_ = "SELECT pelicula FROM Sala "
        salas = consulta(conexion, consulta_)
        salas_ = []
        for peli in salas:
            salas_.append(peli[0])
        # Peliculas:
        sala_etiqueta = ttk.Label(form_frame, text='Peliculas :')
        sala_etiqueta.grid(row=1, column=0, sticky='W', padx=5, pady=10)
        sala_entrada = ttk.Combobox(form_frame, values = salas_)
        sala_entrada.grid(row=1, column=1, sticky='EW', padx=5, pady=10)

        sala_entrada.bind("<<ComboboxSelected>>",lambda event: self.show(event))

        form_frame = tk.Frame(self)
        form_frame.pack(side=tk.BOTTOM)
        #Aceptar
        ttk.Style().configure("TButton", padding=6, relief="flat",background="#ccc")
        aceptar_boton = ttk.Button(form_frame, text='Aceptar')
        aceptar_boton.pack(side=tk.LEFT,padx = 6, pady = 10)
        #Cancelar
        cancelar_boton = ttk.Button(form_frame, text='Cancelar')
        cancelar_boton.pack(side=tk.RIGHT,padx = 6, pady = 10)
