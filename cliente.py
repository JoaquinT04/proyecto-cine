import tkinter as tk
import time
from tkinter import ttk, Button, Frame, messagebox, Tk, Toplevel
from base_de_datos.BDD import crear_conexion, consulta, cerrar
from BDD.consulta_producto import select_producto#, select_producto_by_id
#from BDD.insertar_datos import crear_datos
from clases.Sala import Sala
from reserva import Vent_reserva

class Cliente(Toplevel):
    def __init__(self,root):
        super().__init__(root)
        self.root=root
        self.geometry("960x400")
        self._create_label_input()

    def _create_label_input(self):
        form_frame = tk.Frame(self)
        form_frame.pack()

        sala = Sala()
        conexion = crear_conexion()
        consulta_ = "SELECT pelicula FROM Sala "
        salas = consulta(conexion, consulta_)
        cerrar(conexion)
        salas_ = []
        for peli in salas:
            salas_.append(peli[0])
        salas_2 = []
        for elemento in salas_:
            if elemento not in salas_2:
                salas_2.append(elemento)
        # Peliculas:
        sala_etiqueta = ttk.Label(form_frame, text='Peliculas :')
        sala_etiqueta.grid(row=1, column=0, sticky='W', padx=5, pady=10)
        sala_entrada = ttk.Combobox(form_frame, values = salas_2)
        sala_entrada.grid(row=1, column=1, sticky='EW', padx=5, pady=10)

        sala_entrada.bind("<<ComboboxSelected>>",lambda event: self.show(event))

        seleccionar = ttk.Button(form_frame, text="Seleccionar")
        seleccionar.grid(row=1, column=2, sticky='E', padx=5, pady=10)
        seleccionar['command'] = lambda: seleccionar_()

        def seleccionar_():
            conexion = crear_conexion()
            consulta_ = f"SELECT id_sala FROM Sala WHERE pelicula = '{str(sala_entrada.get())}';"
            ids = consulta(conexion, consulta_)
            lista_ids = []
            for elemento in ids:
                lista_ids.append(elemento[0])
            for i in range(len(lista_ids)):
                consulta_=f"SELECT * FROM Sala WHERE id_sala = {lista_ids[i]}"
                datos = consulta(conexion, consulta_)[0]
                datos = f"ID: {datos[0]}, Formato: {datos[1]}, Pelicula: {datos[2]}, Descuento: {datos[3]}, Precio: {datos[4]}, Horario: {datos[5]}, N° Butacas: {datos[6]}"
                Label = ttk.Label(form_frame, text=datos)
                Label.grid(row=i + 2, column=0, sticky='W', padx=5, pady=10)
                for c in range(5):
                    Label_vacio = ttk.Label(form_frame, text="                                                                                                                                                                                                                  ")
                    Label_vacio.grid(row=i + (c+3), column=0, sticky='W', padx=5, pady=10)



        # form_frame = tk.Frame(self)
        # form_frame.pack(side=tk.BOTTOM)
        #Aceptar
        ttk.Style().configure("TButton", padding=6, relief="flat",background="#ccc")
        aceptar_boton = ttk.Button(form_frame, text='Aceptar')
        aceptar_boton.grid(row=11,column=0,sticky='W', padx=5, pady=10)
        aceptar_boton['command']= lambda: self.abrir_ventana_reserva()
        #Cancelar
        cancelar_boton = ttk.Button(form_frame, text='Cancelar')
        cancelar_boton.grid(row=11,column=2, sticky='E', padx=5, pady=10)
        cancelar_boton['command']= lambda: self.cancelar_()

    def abrir_ventana_reserva(self):
        Vent_reserva(self.root)
    
    def cancelar_(self):
        self.destroy()