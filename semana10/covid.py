#Librerias
import requests

#RUTAS
UrlCovidApi="http://api.covid19api.com/summary"

#funciones
def recuperarUrl(destino,formato):
    consulta = requests.get(destino)

    if (consulta):
        if (consulta.status_code == 200):
            if (formato == "original"):
                return consulta.content
            elif (formato == "texto"):
                return consulta.text
            elif (formato == "json"):
                return consulta.json()
            else:
                return False
        elif (consulta.status_code == 429):
            print ("Demasiadas solicitudes por minuto")
            return False
        else:
            print(f"ERROR al recuperar contenidos: {consulta.message}")
            return False
    else:
        print("ERRROR general en la solicitud")

def buscarPais(consulta,origenDatos):
    i=-1
    for f in origenDatos['Countries']:
        i=i+1
        pais=f"{origenDatos['Countries'][i]['Country']}"

        TotalConfirmados=f"{origenDatos['Countries'][i]['TotalConfirmed']}"
        TotalRecuperados=f"{origenDatos['Countries'][i]['TotalRecovered']}"
        TotalMuertos=f"{origenDatos['Countries'][i]['TotalDeaths']}"

        if pais==consulta :
            consultaDic={}
            consultaDic = {'pais':pais,'TotalConfirmados':TotalConfirmados,'TotalRecuperados':TotalRecuperados,'TotalMuertos':TotalMuertos}
            return consultaDic
            