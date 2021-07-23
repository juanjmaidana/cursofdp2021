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

def buscarPais(consulta):
    i=-1
    for f in datosCovid['Countries']:
        i=i+1
        pais=f"{datosCovid['Countries'][i]['Country']}"
        TotalConfirmados=f"{datosCovid['Countries'][i]['TotalConfirmed']}"
        TotalMuertos=f"{datosCovid['Countries'][i]['TotalDeaths']}"

        if pais==consulta :
            print("COVID19")
            print("-----------------------------")
            print(pais)
            print("-----------------------------")
            print("Total Confirmados: ",TotalConfirmados)
            print("Total Muertos: ",TotalMuertos)
            print("-----------------------------")


   


datosCovid = recuperarUrl(UrlCovidApi)

pais=input("Ingrese nombre del pais: ")
buscarPais(pais)
