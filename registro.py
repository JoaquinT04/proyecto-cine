import tkinter 
from tkinter import ttk, Button, Frame, messagebox, Tk, Toplevel
from base_de_datos.BDD import crear_conexion
from BDD.consulta_usuario import validar_usuario
from BDD.insertar_datos import crear_datos


class CrearCuenta(Toplevel):
    def __init__(self,root):
        super().__init__(root)
        self.root=root
        self.grid()
        self.crear_widgets()
        
        
    def crear_widgets(self):
        ttk.Label(self, text= "Nombre").grid(row=0, column=0)
        ttk.Label(self, text= "Apellido").grid(row=1, column=0)
        ttk.Label(self, text= "DNI").grid(row=3, column=0)
        ttk.Label(self, text= "Contraseña").grid(row=4, column=0)
        
        self.entry_nombre = tkinter.StringVar()
        ttk.Entry(self, textvariable=self.entry_nombre).grid(row=0, column=1)
        
        self.entry_apellido = tkinter.StringVar()
        ttk.Entry(self, textvariable=self.entry_apellido).grid(row=1, column=1)
        
        self.entry_dni = tkinter.IntVar()
        ttk.Entry(self, textvariable=self.entry_dni).grid(row=3, column=1)
        
        self.entry_pass = tkinter.StringVar()
        ttk.Entry(self, textvariable=self.entry_pass).grid(row=4, column=1)
        
        self.button_confirmar= Button(self, text="Confirmar", command=self.crear_usuario).grid(row=5, column=1)
        
        
    def crear_usuario(self):
        conexion = crear_conexion()
        consulta = f"INSERT INTO usuario(Nombre, Apellido,DNI,Contrasenia, Super_Cliente) VALUES('{self.entry_nombre.get()}', '{self.entry_apellido.get()}', {self.entry_dni.get()}, '{self.entry_pass.get()}', '0')"
        crear_datos(conexion, consulta)
        messagebox.showinfo(message="usuario creado correctamente")