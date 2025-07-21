#METHOD RESOLUTION ORDER
#Indica cual es la prioridad para python.
#La funcion super(), utiliza este mro, para dar prioridad a un metodo u otro.
#Heredemos desde donde heredemos, siempre le da prioridad al metodo interno

class A:
    def hablar(self):
        print("Hola desde A")

class B(A):
    def hablar(self):
        print("Hola desde B")

class C(A):
    def hablar(self):
        print("Hola desde C")

class D(B, C):
    def hablar(self):
        print("Hola desde D")


d = D()

d.hablar()

print(D.mro())
