SEMESTRE1 = 183
SEMESTRE2 = 182
ANIO = 365
totalSem1 = 0

#funciones
def cargarDatos(ruta):
    archivo = open(ruta,"r")
    lista = archivo.read().split(",")
    archivo.close()
    
    for indice, item in enumerate(lista):
        lista[indice] = int(item)
    return lista

ingresos = cargarDatos("ingresos.csv")

#Calcular el promedio diario de ingresos del 1er semestre

for i in range(SEMESTRE1):
    totalSem1 = ingresos[i] + totalSem1

promIngresos1 = totalSem1 / SEMESTRE1
print("Promedio Ingreso 1er Semestre: ",int(promIngresos1))

#Calcular el promedio diario de ingresos del 2er semestre
sumIngresos2 = 0

for i in range(184,365):
    sumIngresos2 = ingresos[i] + sumIngresos2

promIngresos2 = sumIngresos2 / 182
print("Promedio Ingreso 2do Semestre: ",int(promIngresos2))

#Promedio diario de todo el año
sumIngresosAnual = 0

for i in range(ANIO):
    sumIngresosAnual = ingresos[i] + sumIngresosAnual

promIngresosAnual = sumIngresosAnual / ANIO
print("Promedio Ingreso Anual: ",int(promIngresosAnual))

#Calcular el % de días en el año, en los que se logró un ingreso mayor o igual a 8000.

ingMayor = 0

for i in range(365):
    if(ingresos[i] >= 8000): ingMayor = ingMayor + 1

porMayor = (ingMayor * 100)/365
print("El",int(porMayor),"% es mayor de 8000")

#monto del día de mayor ingreso y el de menor ingreso.
mayorIngreso = ingresos[0]
menorIngreso = ingresos[0]

for i in range(365):
    if(ingresos[i] >= mayorIngreso): mayorIngreso = ingresos[i]
    elif(ingresos[i] <= menorIngreso): menorIngreso = ingresos[i]

print("El mayor ingreso fue: ",mayorIngreso)
print("El menor ingreso fue: ",menorIngreso)
