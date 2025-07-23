"""Exceptions"""
## TRY  ##EXCEPT

numberOne, numberTwo = 5, 1
print(numberOne + numberTwo) #--> 6

numberTwo = '1' # Cambie el tipo del numero de entero a string.

# ----> print(numberOne + numberTwo) #--> Me produce un ERROR.
# TypeError: unsupported operand type(s) for +: 'int' and 'str'.
# Python no interpreta y se comete un error al intentar sumar un entero con un string, para ello vamos a usar los try & except.

try: 
    print(numberOne + numberTwo) # Se produce el error y pasa al except.
    print("no se ha producido un error")
except:
    print("Se ha producido un error  en la linea 13") # Ejecuta esta linea.
else:
    print('La ejecucion del programa se ejecuto correctamente.') # se ejecuta sino se produuce una excepcion.
finally: 
    print("la ejecucion continua") # se ejecuta Siempre, pase o no una excepcion.
    
# el Else y el finally son opcionales
# El Else solo se ejecuta si no hay una excepcion.
# El finally se ejecuta siempre, exista o no una excepcion.

print('Valor Correcto')
print(numberOne + int(numberTwo))


#captura de excepciones por tipo.
try:
    print(numberOne + numberTwo) 
    print("no se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError en la linea 32")
except TypeError:
    print("Se ha producido un TypeError en la linea 32")
    a = int(numberOne)
    b = int(numberTwo)
    c = a + b
    print(f'corregimos el error de la linea 32 y la suma es igual a {c}')
    
#captura el error con as error

try:
    print(numberOne + numberTwo) 
    print("no se ha producido un error")
except ValueError as error:
    print(error)
except Exception as error:
    print(error)
     
