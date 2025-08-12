intentos = 3
while intentos > 0:
    if input(">>> Escriba la contraseña: ") == "Victordev06":
        print("Ingreso Autorizado!!")
        break
    intentos = intentos - 1
    print(f"Imbecil, te quedan {intentos} intentos")
else:
    print("He eliminado tu usuario por imbecil")

