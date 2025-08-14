from Cities import Cities


# creamos un objeto
ciudades = Cities()

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
        opcion = input("Que opcion deseas?: ").upper()
        if opcion =='I':
            print("**** insertar Paises ****")
            ISO3 = input("introduce la clave ISO3 del nuevo pais: ")
            CountryName = input("introduce el nombre del nuevo pais: ")
            Capital = input("introduce la capital del pais: ")
            CurrencyCode = input("introduce el codigo de su moneda: ")
            r = ciudades.insert_city(ISO3, CountryName, Capital, CurrencyCode)
            if (r==0):
                print("--> No se pudo insertar ningun pais")
            else:
                print("El pais se inserto correctamente")
        elif  opcion =='E':
            print("**** Eliminar Paises ****")
            Id = int(input("introduce el Id del pais que desea eliminar: "))
            r = ciudades.delete_city(Id)
            if(r==0):
                print("EL pais no existe")
            else:
                print("El pais se elimino correctamente")
        elif  opcion =='M':
            print("*** Modificar Paises ***")
        elif  opcion =='P':
            print("*** Imprimir Paises ***")
            print(ciudades)
        elif  opcion =='X':
            print("*** Saliendo del sistema ***")
        else:
            print("-> Invalid option")









if __name__ == "__main__":
    main()