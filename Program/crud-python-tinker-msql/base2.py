import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.constants import INSERT

import mysql.connector
from mysql.connector import Error #==> revisa la conexion remota.import
#libreria para instalar la base de datos
# Debemos ejecutar ==> pip install mysql-connector-python



### --> FUNCIONES

def conectar():
    try:
        conexion = mysql.connector.connect(
            host='localhost', #==> si tienes una remota, aqui va la ruta.
            user = 'root',
            password = "",
            database = 'datospersonales'
        )
        return conexion
    except Error as e:
        messagebox.showerror('Error',str(e))


def insert():
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO misdatos (id, nombre, apellido, telefono, email)VALUES(%s, %s, %s, %s, %s)"  # %s -> inserta los valores
    valores = (entry_id.get(), entry_nombre.get(), entry_apellido.get(), entry_telefono.get(), entry_email.get())
    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo('informacion','registro insertado con exito!')
        limpiar_campos()
    except Error as e:
        messagebox.showerror('Error',str(e))
    finally:
        conexion.close()

#siempre debemos cerrar la conexion a la base de datos. finally -> conexion.close()


def editar():
    conexion = conectar()
    cursor = conexion.cursor()
    sql ="UPDATE misdatos SET id=%s, nombre=%s, apellido=%s, telefono=%s, email=%s WHERE email=%s"

def delete():
    pass

def buscar():
    pass

def clear():
    pass

def limpiar_campos():
    pass

#importamos de tk, ttk y messagebok de la libreria tkinter

### --> FORMULARIO.

#Creamos el formulario.
app = tk.Tk() #creamos una llamada a la ventana
app.title('formulario de datos personales') #titulo de la tabla

#creamos los elementos del formulario
ttk.Label(app, text='ID: ').grid(column=0, row=0)
entry_id = ttk.Entry(app)
entry_id.grid(column=1, row=0)

ttk.Label(app, text='Nombre: ').grid(column=0, row=1)
entry_nombre=ttk.Entry(app)
entry_nombre.grid(column=1, row=1)

ttk.Label(app, text='Apellido: ').grid(column=0, row=2)
entry_apellido = ttk.Entry(app)
entry_apellido.grid(column=1, row=2)

ttk.Label(app, text='Telefono: ').grid(column=0, row=3)
entry_telefono=ttk.Entry(app)
entry_telefono.grid(column=1, row=3)

ttk.Label(app, text='Email: ').grid(column=0, row=4)
entry_email=ttk.Entry(app)
entry_email.grid(column=1, row=4)

ttk.Button(app, text='insert', command=insert).grid(column=0, row=5)
ttk.Button(app, text='editar', command=editar).grid(column=1, row=5)
ttk.Button(app, text='eliminar', command=delete).grid(column=2, row=5)
ttk.Button(app, text='buscar', command=buscar).grid(column=3, row=5)
ttk.Button(app, text='limpiar', command=clear).grid(column=4, row=5)



app.mainloop()
#tabla en min.6:47

