import pandas as pd
from pandas.core.indexes.base import Index

lista = pd.read_csv("ingresos.csv",delimiter=",")
cantidad = len(lista.axes[1])
listaInt = []
#for i in range(365): 
#    listaInt[i] = int(lista[i])

print(lista[0])
