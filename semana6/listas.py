# mtrDatos = []

# archivosDatos = open("ingresos.csv", "r")
# mtrDatos = archivosDatos.read().split(",")
# archivosDatos.close()

# mtrDatos.sort()

# print(mtrDatos)

#Cargar el paquete de reportes en una lista
lista = open("ingresos.csv","r")
#Calcular el promedio diario de ingresos del 1er semestre
ingresos = []
ingresos = lista.read().split(",")
sumIngresos = 0

for i in range(183):
    sumIngresos = int(ingresos[i]) + sumIngresos

promIngresos1 = sumIngresos / 183
print("Promedio Ingreso 1er Semestre: ",round(promIngresos1))

#Calcular el promedio diario de ingresos del 2er semestre
sumIngresos2 = 0

for i in range(184,365):
    sumIngresos2 = int(ingresos[i]) + sumIngresos2

promIngresos2 = sumIngresos2 / 182
print("Promedio Ingreso 2do Semestre: ",round(promIngresos2))

#Promedio diario de todo el año
sumIngresosAnual = 0

for i in range(365):
    sumIngresosAnual = int(ingresos[i]) + sumIngresosAnual

promIngresosAnual = sumIngresosAnual / 365
print("Promedio Ingreso Anual: ",round(promIngresosAnual))

#Calcular el % de días en el año, en los que se logró un ingreso mayor o igual a 8000.
ingMayor = 0
for i in range(365):
    if(int(ingresos[i])>=8000): ingMayor = ingMayor + 1
porMayor = (ingMayor * 100)/365
print("El",round(porMayor),"% es mayor de 8000")

#monto del día de mayor ingreso y el de menor ingreso.
mayorIngreso = int(ingresos[0])
menorIngreso = int(ingresos[0])

for i in range(365):
    if(int(ingresos[i]) >= mayorIngreso): mayorIngreso = int(ingresos[i])
    elif(int(ingresos[i]) <= menorIngreso): menorIngreso = int(ingresos[i])

print("El mayor ingreso fue: ",mayorIngreso)
print("El menor ingreso fue: ",menorIngreso)
