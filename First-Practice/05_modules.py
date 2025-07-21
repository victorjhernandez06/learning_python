
## Módulos
## Modules
## Podemos importar trozos de código desde un archivo en específico.
## We can import snippets of code from a specific file
## -> import modulo as supermodule


## Para importar funciones especificas
## To import specific functions
## -> from modulo import funcion1, function2

from firstPractice import operations

res_suma = operations.sumar(2, 1)
print(res_suma)

res_multi = operations.multiplicar(10, 2, 1)
print(res_multi)

