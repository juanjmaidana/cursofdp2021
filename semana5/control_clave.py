clave = "Juan2020"

for i in range (1,4):
    ingClave = input("Ingrese Clave: ")
    if(ingClave == clave):
        print("Clave Correcta!!!")
        break
    else:
        print("Clave Incorrecta") 
        print("Intentos Restantes: ",3 - i)
    
    if (i == 3): 
        print("")
        print("Clave incorrecta intente mas tarde!!!")


