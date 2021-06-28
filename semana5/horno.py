import random

while(True):
  
  tempObjetivo = 0
  totalLectura = 0
  promLectura = 0

  tempObjetivo = random.randint(100,200)
  print("Temperatura Objetivo: ",tempObjetivo)
  tempPrueba = 1
  
  while(tempPrueba <= 100 or tempPrueba >= 200) and tempPrueba != 0:
    tempPrueba = int(input("Ingrese Temperatura: "))
     
  if(tempPrueba == 0): 
    print("Programa Finalizado") 
    break

  for i in range(10):
    lectura = random.randint(tempObjetivo - 2,tempObjetivo + 2)
    totalLectura = totalLectura + lectura

  promLectura = totalLectura / 10
  
  print()
  print("Promedio de Lecturas: ",int(promLectura))

  if (promLectura < tempObjetivo):
    print("Temperatura baja, se enciende quemador")
  elif (promLectura > tempObjetivo):
    print("Temperatura alta, se apaga quemador")
  else:
    print("Temperatura Estable")

  print()
  print("**************************************************")
  