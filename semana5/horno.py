import random

while(True):
  
  totalLectura = 0
  promLectura = 0

  #temperatura de objetivo al azar
  tempObjetivo = random.randint(100,200 + 1)
  print("Temperatura Objetivo: ",tempObjetivo)
    
  #ingreso de te temperatura de prueba
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
  