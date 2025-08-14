from Cities import Cities


# creamos un objeto
cuidades = Cities()

menu = """
**************************
*    MENU CIUDADES       *
**************************
*                        *
* i) Insertar Ciudades   *
* e) Eliminar Registro   *
* m) Modificar Registros *
* p) Imprimir la Tabla   *
* x) Salir               *
*                        *   
**************************
"""


def main():
    opcion = '0'
    while opcion != 'X':
        print(menu)
        opcion = input("Que opcion deseas?").upper()
        if opcion =='I':
            print("**** insertar Paises ****")
        elif  opcion =='E':
            print("**** Eliminar Paises ****")
        elif  opcion =='M':
            print("*** Modificar Paises ***")
        elif  opcion =='P':
            print("*** Imprimir Paises ***")
        elif  opcion =='X':
            print("*** Saliendo del sistema ***")
        else:
            print("-> Invalid option")









if __name__ == "__main__":
    main()