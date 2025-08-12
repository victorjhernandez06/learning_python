class Gato():
       def sonido(self):
        return "Miau"

class Perro():
    def sonido(self):
        return "Guau"

def hacer_sonido(animal):
    print(animal.sonido())

    perro = Perro()
    gato = Gato()

    print(perro.sonido())
    print(gato.sonido())

    hacer_sonido(gato)
    hacer_sonido(perro)

    def recorrer (elemento):
        for item in elemento:
            print (f"El elemento actual es: {item}")


    lista = [1,2,3,4]
    lista2 = "maquina"

    recorrer(lista)


class Bird:
    def fly(self):
        print("Fly with wings")

class Airplane:
    def fly(self):
        print("Fly with fuel")

class Fish:
    def swin(self):
        print("fish swin in sea")
    def fly(self):
        print("Some fish can fly")

#attributes having same name are
#considered as duck typing

for obj in Bird(), Airplane(), Fish():
    obj.fly()


class Special_string:
    def __len__(self):
        return 21

#drive's code
if __name__ == "__main__":
    string = Special_string()
    print(len(string))

