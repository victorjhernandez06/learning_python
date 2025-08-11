from tkinter import*
from ventana import*



#01 Creamos la funcion main
def main():
    root = Tk()
    root.wm_title("Crud Python MySql")
    app = Ventana(root) # --> esta clase esta dentro de otro archivo, llamado ventana.
    app.mainloop()

if __name__ == "__main__":
    main()