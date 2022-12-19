import tkinter 
from tkinter import ttk, Button, Frame, messagebox, Tk, Toplevel
from cliente import Cliente
from base_de_datos.BDD import crear_conexion
from BDD.consulta_usuario import validar_usuario

class Login(Toplevel):
    def __init__(self,root):
        super().__init__(root)
        self.root=root
        self.grid()
        self.crear_widgets()
        
        
    def crear_widgets(self):
        ttk.Label(self, text= "DNI").grid(row=1, column=0)
        #ttk.Label(self, text= "Apellido").grid(row=2, column=0)
        ttk.Label(self,text="Contraseña").grid(row=3, column=0)
        
        
        self.entry_DNI = tkinter.StringVar()
        ttk.Entry(self, textvariable= self.entry_DNI).grid(row=1, column=1)
        
        # self.entry_apellido = tkinter.StringVar()
        # ttk.Entry(self, textvariable= self.entry_apellido).grid(row=2, column=1)
        
        self.entry_pass = tkinter.StringVar()
        ttk.Entry(self, textvariable= self.entry_pass).grid(row=3, column=1)
        
        ttk.Button(self, text="ingresar", command=self.verificar_datos).grid(row=4, column=1)
    
    
    def verificar_datos(self):
        conexion = crear_conexion()
        consulta = f"SELECT * FROM Usuario WHERE DNI = '{self.entry_DNI.get()}' and Contrasenia= '{self.entry_pass.get()}'"
        respuesta=validar_usuario(conexion, consulta)
        if respuesta:
            #messagebox.showinfo(message='usuario correcto')
            self.abrir_ventana_cliente()
        else:
            messagebox.showerror(message='usuario incorrecto')
            
    def abrir_ventana_cliente(self):
        Cliente(self.root)