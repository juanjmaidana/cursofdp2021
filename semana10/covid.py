#Librerias
import requests


#RUTAS
UrlCovidApi="http://api.covid19api.com/summary"

#funciones
def recuperarUrl(destino):
    consulta = requests.get(destino)

    if(consulta):
        if(consulta.status_code==200):
            return consulta.json()


   


datosCovid = recuperarUrl(UrlCovidApi)


paises = f'{datosCovid["C"][0]}'
print(paises)
 

