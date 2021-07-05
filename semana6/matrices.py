# Ejemplo de Lista "mutable" puedo agregar y modificar

# cont = 0
# lista = []

# while(True):
#     ingNum = int(input("Ingrese un numero a la matriz: "))
#     if(ingNum == 0):
#         break
#     lista.append(ingNum)
#     cont = cont + 1

# for i in range(cont):
#     print(lista[i])

#TUPLA inmutable no puedo cambiar.

# tuplaVariante = (23,15,20,3)
# print(tuplaVariante)
# print(tuplaVariante[3])

#Diccionarios parcialmente inmutables

datosPersonales = {"Nombre:": "Juan José", "Apellido ": "Maidana", "Edad:":40, "Legajo":1000}
datosPersonales["Edad:"] = input("Ingrese edad:")
print(datosPersonales)
print(datosPersonales["Nombre:"])

