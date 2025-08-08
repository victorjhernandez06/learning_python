import tkinter as tk
from tkinter import ttk, messagebox

#importamos de tk, ttk y messagebok de la libreria tkinter

#Creamos el formulario.
app = tk.Tk() #creamos una llamada a la ventana
app.title('formulario de datos personales') #titulo de la tabla

#creamos los elementos del formulario
ttk.Label(app, text="ID: ").grid(column=0, row=0)
entry_id=ttk.Entry(app)
entry_id.grid(colum=1, row=0)

ttk.Label(app, text="ID: ").grid(column=0, row=0)

app.mainloop()
#tabla en min.6:47

