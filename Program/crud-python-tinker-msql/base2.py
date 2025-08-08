import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.constants import INSERT

import mysql.connector
from mysql.connector import Error #==> revisa la conexion remota.import
#libreria para instalar la base de datos
# Debemos ejecutar ==> pip install mysql-connector-python


### --> FUNCIONES
"""
## En todas las interacciones de agregar, actualizar, buscar y borrar, antes del try:
conexion = conectar()
cursor = conexion.cursor()

## Al finalizar el try:
finally:
        conexion.close()
        
#importamos de tk, ttk y messagebok de la libreria tkinter
"""

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


def actualizar():
    conexion = conectar()
    cursor = conexion.cursor()
    sql ="UPDATE misdatos SET nombre=%s, apellido=%s, telefono=%s, email=%s WHERE id=%s"
    valores = (entry_id.get(), entry_nombre.get(), entry_apellido.get(), entry_telefono.get(), entry_email.get())
    try:
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo('Informacion',"Registro actualizado con exito!")
        limpiar_campos()
    except Error as e:
        messagebox.showerror('Error',str(e))
    finally:
        conexion.close()

def delete():
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM misdatos Where id=%s"
    try:
        cursor.execute(sql,(entry_id.get(),))
        conexion.commit()
        messagebox.showinfo('informacion','Registro eliminado con exito')
        limpiar_campos()
    except Error as e:
        messagebox.showerror('Error',str(e))
    finally:
        conexion.close()


def buscar():
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "SELECT * FROM misdatos WHERE id=%s"
    try:
        cursor.execute(sql,(entry_id.get(),))
        registro = cursor.fetchone()
        if registro:
            entry_nombre.insert(0, registro[1])
            entry_apellido.insert(0, registro[2])
            entry_telefono.insert(0, registro[3])
            entry_email.insert(0, registro[4])
        else:
            messagebox.showinfo('Informacion', 'No se encontro el registro solicitado')
    except Error as e:
        messagebox.showerror('Error',str(e))
    finally:
        conexion.close()


def limpiar_campos():
   entry_id.delete(0, tk.END)
   entry_nombre.delete(0, tk.END)
   entry_apellido.delete(0, tk.END)
   entry_telefono.delete(0, tk.END)
   entry_email.delete(0, tk.END)

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
ttk.Button(app, text='actualizar', command=actualizar).grid(column=1, row=5)
ttk.Button(app, text='eliminar', command=delete).grid(column=2, row=5)
ttk.Button(app, text='buscar', command=buscar).grid(column=3, row=5)
ttk.Button(app, text='limpiar', command=limpiar_campos).grid(column=4, row=5)


app.mainloop()
#tabla en min.6:47

