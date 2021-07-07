import re

archivo = open("clima.csv", "r")
lista = archivo.readlines() #readlines lee por lineas.

for i, linea in enumerate(lista):
    if(re.match("^SAUCE VIEJO AERO\\tP", linea)):
        datos = linea.removesuffix("\n").split("\t")
dic = {"Ciudad:":datos[0], "Tipo de registro:":datos[1]}
print(dic)