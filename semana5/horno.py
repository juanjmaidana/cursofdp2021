import random

while(True):
  
  totalLectura = 0
  promLectura = 0

  #temperatura de objetivo al azar
  tempObjetivo = random.randint(100,200 + 1)
  print("Temperatura Objetivo: ",tempObjetivo)
    
  #ingreso de te temperatura de prueba
  tempPrueba = int(input("Ingrese Temperatura de Prueba: "))
  if(tempPrueba == 0): 
    print("Programa Finalizado") 
    break
  
  if (tempPrueba >= 100 and tempPrueba <= 200):
    #print("Temperatura de Prueba: ",tempPrueba)
  
    for i in range(10):
     lectura = random.randint(tempObjetivo - 2,tempObjetivo + 2)
     totalLectura = totalLectura + lectura
     promLectura = totalLectura / 10
  
    print("****************************************************")
    print("Promedio de Lecturas: ",int(promLectura))

    if (promLectura < tempObjetivo):
      print("Temperatura baja, se enciende quemador")
      print("*******************************************************")
    elif (promLectura > tempObjetivo):
      print("Temperatura alta, se apaga quemador")
      print("*******************************************************")

  else:
    print("Fuera de Rango")
    print()
  