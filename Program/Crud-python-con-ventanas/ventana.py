from tkinter import*


class Ventana(Frame):
    #llamamos al constructor con el ancho de las ventanas
    def __init__(self, master = None):
        super().__init__(master, width=680, height=260)
        self.master = master
        self.pack()
        self.create_widgets()

    def fNuevo(self):
        pass

    def fmodificar(self):
        pass

    def fEliminar(self):
        pass

    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0, y=0, width=93, height=259)

        self.btnNuevo =  Button(frame1, text = "Nuevo", command=self.fNuevo, bg="blue", fg="white")
        self.btnNuevo.place(x=5, y=50, width=80, height=30)

        self.btnModificar = Button(frame1, text="Modificar", command=self.fmodificar(), bg="blue", fg="white")
        self.btnModificar.place(x=5, y=90, width=80, height=30)

        self.btnEliminar = Button(frame1, text="Eliminar", command=self.fNuevo, bg="blue", fg="white")
        self.btnEliminar.place(x=5, y=130, width=80, height=30)



