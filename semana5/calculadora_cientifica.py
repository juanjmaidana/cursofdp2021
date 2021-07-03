import math
while(True):
    numero = int(input("Ingresar Número: "))
    print()
    print("1. seno")
    print("2. coseno")
    print("3. tangente")
    print("4. raíz cuadrada")
    print()
    print("0. SALIR")
    print()
    opc = int(input("Ingrese N° de operación: "))
    
    if(opc == 0):
        break
    elif(opc == 1):
        resultado = math.sin(numero)
    elif(opc == 2):
        resultado = math.cos(numero) 
    elif(opc == 3):
        resultado = math.tan(numero)
    elif(opc == 4):
        resultado = math.sqrt(numero)
    print()
    print("Resultado: ",resultado)
    print()

print()
print("Calculadora Finalizada")